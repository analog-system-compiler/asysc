# Copyright (C) 2006-2026 The ASysC project
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <https://www.gnu.org/licenses/>.

from numbers import Integral, Real

import numpy as np


def _is_finite_real(value):
    return (
        isinstance(value, Real)
        and not isinstance(value, bool)
        and np.isfinite(value)
    )


class element:
    def __init__(self, name):
        self.name = name
        self.value_y_init = 0.0
        self._clear()

    def _clear(self):
        self.dy = 0
        self.value_y_prev = self.value_y_init
        self.value_y = self.value_y_init
        self.dydx = 2.0 / 1e-9
        self.history_x = []
        self.history_y = []

    def init(self, value):
        self.value_y_init = value


class circuit_base:
    def __init__(self):
        self._clear()

    def _elements(self):
        return [
            value for value in self.__dict__.values() if isinstance(value, element)
        ]

    def _clear(self):
        self.timeval = 0.0
        self.delta_timeval = 0.0
        self.conv = False
        for e in self._elements():
            e._clear()

    def _time(self):
        return self.timeval

    def _delay(self, element_arg, delay_arg):
        if element_arg.history_x:
            return np.interp(
                self.timeval - delay_arg,
                element_arg.history_x,
                element_arg.history_y,
            )
        return 0.0

    def _getv(self, element_arg):
        return element_arg.value_y

    def _last(self, element_arg):
        return element_arg.value_y_prev

    def _der0(self, element_arg):
        return element_arg.dy

    def _der1(self, element_arg):
        return element_arg.dydx

    def _setc(self, element_arg, val):
        element_arg.value_y = val

    def _setf(self, element_arg, val, f):
        element_arg.history_x.append(f)
        element_arg.history_y.append(val)

    def _step_t(self):
        t = self.timeval
        for e in self._elements():
            if e.history_x:
                delta_t = t - e.history_x[-1]
                dydx_prev = e.dydx
                e.dydx = 2.0 / delta_t
                e.dy = -(e.dydx * e.value_y + dydx_prev * e.value_y + e.dy)
            e.history_x.append(t)
            e.history_y.append(e.value_y)

    def _step_c(self):
        for e in self._elements():
            e.value_y_prev = e.value_y * self.res + e.value_y_prev * (1 - self.res)
            if e.value_y_prev == 0:
                error = abs(e.value_y - e.value_y_prev)
            else:
                error = abs((e.value_y - e.value_y_prev) / e.value_y_prev)
            if error > self.res:
                self.conv = False

    def simulate_t(self, duration, nb=500, res=1, max_iter=1):
        if not _is_finite_real(duration) or duration <= 0:
            raise ValueError("duration must be a finite positive number")
        if not isinstance(nb, Integral) or isinstance(nb, bool) or nb <= 0:
            raise ValueError("nb must be a positive integer")
        if not _is_finite_real(res) or not 0 < res <= 1:
            raise ValueError("res must be a finite number in the range (0, 1]")
        if (
            not isinstance(max_iter, Integral)
            or isinstance(max_iter, bool)
            or max_iter <= 0
        ):
            raise ValueError("max_iter must be a positive integer")

        self._clear()
        self.delta_timeval = duration / nb
        self.res = res
        self.max_iter = max_iter
        for i in range(nb):
            self.conv = False
            iter_nb = 0
            while not self.conv and iter_nb < self.max_iter:
                self.conv = True
                self.compute_t()
                self._step_c()
                iter_nb += 1
            self._step_t()
            self.timeval += self.delta_timeval
            print(
                "Iteration: {}/{}, steps: {}   ".format(i + 1, nb, iter_nb),
                end="\r",
            )

    def simulate_f(self, start, end, nb):
        if not _is_finite_real(start) or start <= 0:
            raise ValueError("start must be a finite positive frequency")
        if not _is_finite_real(end) or end < start:
            raise ValueError(
                "end must be a finite frequency greater than or equal to start"
            )
        if not isinstance(nb, Integral) or isinstance(nb, bool) or nb <= 0:
            raise ValueError("nb must be a positive integer")

        self._clear()
        for i, self.freq in enumerate(np.geomspace(start, end, nb)):
            self.s = 2j * np.pi * self.freq
            self.compute_f()
            print("Iteration: {}/{}".format(i + 1, nb), end="\r")
