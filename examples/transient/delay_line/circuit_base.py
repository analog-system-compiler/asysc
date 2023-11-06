# import math
import numpy as np

class element:
  
    def __init__(self, name):
        self.history_x = [0]
        self.history_y = [0]
        self.dydx = 2.0 / 1e-9
        self.dy = 0
        self.dydx_prev = 0
        self.dy_prev = 0
        self.name = name

    def set(self, val):
        self.value_y = val
        
    def step(self, t):
        delta_t = t - self.history_x[-1]
        if delta_t:
            self.dydx = 2.0 / delta_t
            self.dy = - ( self.dydx * self.value_y + self.dydx_prev * self.value_y + self.dy_prev )
        self.dydx_prev = self.dydx
        self.dy_prev = self.dy
        self.history_x.append(t)
        self.history_y.append(self.value_y)

class circuit_base:
    
    delta_timeval = 1e-9
    timeval = 0.0

    def __init__(self):
        self.timeval = 0.0
        self.delta_timeval = 0.0

    def delta_time(self):
        return self.delta_timeval

    def time(self):
        return self.timeval

    def _delay(self, element_arg, delay_arg):
        return np.interp(self.timeval - delay_arg, element_arg.history_x, element_arg.history_y)

    def _der0(self, element_arg):
        return element_arg.dy

    def _der1(self, element_arg):
        return element_arg.dydx

    def simulate(self, duration, nb):
        self.delta_timeval = duration / nb
        for i in range(0, nb):
            self.step()
            self.timeval += self.delta_timeval
            print("Iteration nb {}".format(i), end="\r")
