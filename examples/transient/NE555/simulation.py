
#!/usr/bin/python3

import math
import numpy as np
import matplotlib.pyplot as plt
import NE555
import circuit_base
from NE555 import circuit
from circuit_base import circuit_base, element

ylabel = []
def add_plot( element ):
    plt.plot( element.history_x, element.history_y )
    ylabel.append(element.name)

my_circuit = circuit()
my_circuit.simulate_t(0.1,1000,1/10,10)

plt.subplot(1, 1 , 1)
add_plot( my_circuit.IC_UTRESH  )
add_plot( my_circuit.IC_UOUT  )
ax = plt.gca()
ax.set_ylabel('Voltage [V]')
plt.legend(ylabel)

ax.set_xlabel('Time [s]')
plt.grid(True)
plt.show()