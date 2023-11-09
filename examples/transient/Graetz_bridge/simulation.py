
#!/usr/bin/python3

import math
import numpy as np
import matplotlib.pyplot as plt
import graetz_bridge
import circuit_base
from graetz_bridge import circuit
from circuit_base import circuit_base, element

ylabel = []
def add_plot( axs, element ):
    axs.plot( element.history_x, element.history_y )
    ylabel.append(element.name)

my_circuit = circuit()
#my_circuit.simulate_t(1e-3,1000)
my_circuit.simulate_t(1e-3,1000)
# print(my_circuit.R1_U.history_y)
# print(my_circuit.V_U .history_y)
# print(my_circuit.D1_U.history_y)
# print(my_circuit.D2_U.history_y)
# print(my_circuit.D3_U.history_y)
# print(my_circuit.D4_U.history_y)
# print(my_circuit.R2_U.history_y)
# print(my_circuit.C_U .history_y)

fig, axs = plt.subplots(1, 1)
add_plot( axs, my_circuit.V_U )
add_plot( axs, my_circuit.R1_U )
#add_plot( axs, my_circuit.D1_U )
# add_plot( axs, my_circuit.D2_U )
# add_plot( axs, my_circuit.D3_U )
#add_plot( axs, my_circuit.D4_U )
#add_plot( axs, my_circuit.R2_U )
# add_plot( axs, my_circuit.C_U )
axs.set_xlabel('Time (s)')
axs.set_ylabel('V')
axs.legend(ylabel)
axs.grid(True)

plt.show()