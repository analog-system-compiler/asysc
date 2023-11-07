# import math
import numpy as np


class element:

    element_list = []

    def __init__(self, name):
        self.name = name
        self.element_list.append(self)
        self.history_x = [0]
        self.history_y = [0]
        self.dydx = 2.0 / 1e-9
        self.dy = 0
        self.dydx_prev = 0
        self.dy_prev = 0
        self.value_y = 0.0

    def set_t(self, val):
        self.value_y = val

    def set_f(self, val, f):
        self.history_x.append(f)
        self.history_y.append(val)

    def step_t(t):
        for e in element.element_list:
            delta_t = t - e.history_x[-1]
            if delta_t:
                e.dydx = 2.0 / delta_t
                e.dy = -(e.dydx * e.value_y + e.dydx_prev * e.value_y + e.dy_prev)
            e.dydx_prev = e.dydx
            e.dy_prev = e.dy
            e.history_x.append(t)
            e.history_y.append(e.value_y)


class circuit_base:

    def __init__(self):
        self.timeval = 0.0
        self.delta_timeval = 0.0

    def delta_time(self):
        return self.delta_timeval

    def time(self):
        return self.timeval

    def _delay(self, element_arg, delay_arg):
        return np.interp(
            self.timeval - delay_arg, element_arg.history_x, element_arg.history_y
        )

    def _get(self, element_arg):
        return element_arg.value_y
    
    def _der0(self, element_arg):
        return element_arg.dy

    def _der1(self, element_arg):
        return element_arg.dydx

    def simulate_t(self, duration, nb):
        self.delta_timeval = duration / nb
        for i in range(0, nb):
            self.step()
            element.step_t(self.timeval)
            self.timeval += self.delta_timeval
            print("Iteration nb {}".format(i), end="\r")

    def simulate_f(self, start, end, nb):
        log_end = np.log10(2 * np.pi * end)
        for i in range(0, nb):
            self.freq = start * 10 ** ((i * log_end) / nb)
            self.s = 2j * np.pi * self.freq
            self.step()
            print("Iteration nb {}".format(i), end="\r")
