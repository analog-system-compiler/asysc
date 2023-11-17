
#!/usr/bin/python3

import math
import numpy as np
import matplotlib.pyplot as plt
import graetz_bridge
import circuit_base
from graetz_bridge import circuit
from circuit_base import circuit_base, element

ylabel = []
def add_plot( element ):
    plt.plot( element.history_x, element.history_y )
    ylabel.append(element.name)

my_circuit = circuit()
my_circuit.simulate_t(1e-3,1000)

plt.subplot(2, 1 , 1)
add_plot( my_circuit.V_U )
add_plot( my_circuit.R1_U )
ax = plt.gca()
ax.set_ylabel('Voltage [V]')
plt.subplot(2, 1 , 2)
add_plot( my_circuit.R2_I )
ax = plt.gca()
ax.set_xlabel('Time [s]')
ax.set_ylabel('Intensity [A]')
plt.legend(ylabel)
plt.grid(True)

plt.show()