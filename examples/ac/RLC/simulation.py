
#!/usr/bin/python3

import math
import numpy as np
import matplotlib.pyplot as plt
import RLC

from RLC import circuit
from circuit_base import circuit_base, element

ylabel = []

def add_gain_plot(axs, element):
    axs.plot(element.history_x, 20 * np.log10(np.absolute(element.history_y)))
    ylabel.append(element.name)


my_circuit = circuit()
my_circuit.simulate_f(1, 1e6, 1000)

fig, axs = plt.subplots(1, 1, layout="constrained")
add_gain_plot(axs, my_circuit.R_U)
add_gain_plot(axs, my_circuit.L_U)
add_gain_plot(axs, my_circuit.C_U)
axs.set_xlabel("Freq (Hz)")
axs.set_ylabel("Gain")
axs.legend(ylabel)
axs.grid(True)
axs.set_xscale('log')

plt.show()
