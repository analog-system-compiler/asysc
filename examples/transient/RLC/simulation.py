
import math
import numpy as np
import matplotlib.pyplot as plt
import RLC
import circuit_base
from RLC import circuit
from circuit_base import circuit_base, element

ylabel = []
def add_plot( axs, element ):
    axs.plot( element.history_x, element.history_y )
    ylabel.append(element.name)

my_circuit = circuit()
my_circuit.simulate(1e-6,1000)

fig, axs = plt.subplots(1, 1, layout='constrained')
add_plot( axs, my_circuit.R1_U )
add_plot( axs, my_circuit.R2_U )
#add_plot( axs, my_circuit.R3_U )
add_plot( axs, my_circuit.C1_U )
add_plot( axs, my_circuit.VP_U )
axs.set_xlabel('Time (s)')
axs.set_ylabel('V')
axs.legend(ylabel)
axs.grid(True)

plt.show()