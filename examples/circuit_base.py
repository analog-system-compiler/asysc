# Copyright (C) 2006-2024 The ASysC project                        
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
# along with this program; If not, see <https://www.gnu.org/licenses/>

# import math
import numpy as np

class element:
    
    element_list = []

    def __init__(self, name):
        element.element_list.append(self)
        self.name = name        
        self.history_x = []
        self.history_y = []
        self.dydx = 2.0 / 1e-9
        self.dy = 0
        self.dydx_prev = 0
        self.dy_prev = 0
        self.value_y_prev = 0.0
        self.value_y = 0.0


class circuit_base:

    def __init__(self):
        self.timeval = 0.0
        self.delta_timeval = 0.0
        self.conv = False

    def _clear(self):
        for e in element.element_list:
            e.history_x = []
            e.history_y = []

    def _time(self):
        return self.timeval

    def _delay(self, element_arg, delay_arg):
        if element_arg.history_x:
            return np.interp( self.timeval - delay_arg, element_arg.history_x, element_arg.history_y )
        return 0.0

    def _getv(self, element_arg):
        return element_arg.value_y

    def _last(self, element_arg):
        if element_arg.value_y_prev == 0:
            self.conv = False
        else:
            error = abs( (element_arg.value_y - element_arg.value_y_prev) / element_arg.value_y_prev )            
            if error > self.res:
                self.conv = False
                #print(error)
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
        t=self.timeval
        for e in element.element_list:
            if e.history_x:
                delta_t = t - e.history_x[-1]
                e.dydx = 2.0 / delta_t
                e.dy = -(e.dydx * e.value_y + e.dydx_prev * e.value_y + e.dy_prev)
            e.dydx_prev = e.dydx
            e.dy_prev = e.dy
            e.history_x.append(t)
            e.history_y.append(e.value_y)

    def _step_c(self):
        for e in element.element_list:
            e.value_y_prev = e.value_y * self.res + e.value_y_prev * (1 - self.res)

    def simulate_t(self, duration, nb=500, res=1, max_iter=1):
        self._clear()
        self.delta_timeval = duration / nb
        self.res = res
        self.max_iter = max_iter
        for i in range(0, nb):
            self.conv = False
            iter_nb = 0
            while not self.conv and iter_nb < self.max_iter:
                self.conv = True
                self.step()
                self._step_c()
                iter_nb += 1
            self._step_t()
            self.timeval += self.delta_timeval
            print("Iteration: {}/{}, steps: {}   ".format(i+1, nb, iter_nb), end="\r")

    def simulate_f(self, start, end, nb):
        self._clear()
        log_end = np.log10(end)
        log_start = np.log10(start)
        for i in range(0, nb):
            self.freq = 10 ** (log_start + ((i * (log_end-log_start)) / nb))
            self.s = 2j * np.pi * self.freq
            self.step()
            print("Iteration: {}/{}".format(i+1, nb), end="\r")
