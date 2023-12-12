
#!/usr/bin/python3

import math
import numpy as np
import matplotlib.pyplot as plt
import NPN
import circuit_base
from NPN import circuit
from circuit_base import circuit_base, element


def add_plot( element ):
    plt.plot( element.history_x, element.history_y )
    ylabel.append(element.name)

my_circuit = circuit()
my_circuit.simulate_t(2,1000)

plt.subplot(2, 1, 1)
ylabel = []
add_plot( my_circuit.P1_U )
add_plot( my_circuit.P2_U )
ax = plt.gca()
ax.set_ylabel('Voltage [V]')
plt.legend(ylabel)
plt.grid(True)

plt.subplot(2, 1, 2)
ylabel = []
add_plot( my_circuit.Q1_IBE )
ax = plt.gca()
ax.set_xlabel('Time [s]')
ax.set_ylabel('Intensity [A]')
plt.legend(ylabel)
plt.grid(True)

plt.show()