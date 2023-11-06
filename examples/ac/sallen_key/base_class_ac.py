import numpy as np

class element:
  
    def __init__(self, name):
        self.history_x = []
        self.history_y = []
        self.value_y = 0.0 + 0.0j

    def set(self, val):
        self.value_y = val
        
    def step(self, f):
        self.history_x.append(f)
        self.history_y.append(self.value_y)

class circuit_base:
    
    def __init__(self):
        self.p = 0.0 + 0.0j

    def simulate(self, start, end, nb):
        log_end = np.log10(2*np.pi*end)
        for i in range(0, nb):
            omega = 2*np.pi*start*10**((i*log_end)/nb)
            self.p = omega * 1j
            print("Iteration nb {}".format(i), end="\r")

