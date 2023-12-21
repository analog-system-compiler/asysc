
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
my_circuit.simulate_t(0.1,1000)

plt.subplot(1, 1 , 1)
#add_plot( my_circuit.P1_U )
#add_plot( my_circuit.IC_UTRIG )
add_plot( my_circuit.IC_UTRESH  )
#add_plot( my_circuit.P2_U  )
#add_plot( my_circuit.IC_UIN1  )
#   add_plot( my_circuit.IC_UIN2  )
#add_plot( my_circuit.IC_SR_Uin2  )
#add_plot( my_circuit.IC_SR_Uin1  ) 
#add_plot( my_circuit.IC_UOUT  )
#add_plot( my_circuit.IC_SR_Uout  ) 
#add_plot( my_circuit.IC_UOUT2  )
add_plot( my_circuit.IC_UOUT  )
#add_plot( my_circuit.RA_U  )
#add_plot( my_circuit.IC_VCC  )
#add_plot( my_circuit.RB_U  )

#add_plot( my_circuit.C1_U  )
#add_plot( my_circuit.V1_U  )
#add_plot( my_circuit.V1_I  )
ax = plt.gca()
ax.set_ylabel('Voltage [V]')
plt.legend(ylabel)

# ylabel = []
# plt.subplot(2, 1 , 2)
# add_plot( my_circuit.IC_SW_I  )
# #add_plot( my_circuit.C1_I  )
# #add_plot( my_circuit.RA_I  )
# #add_plot( my_circuit.IC_SR_Iout  )
# #add_plot( my_circuit.RB_I  )
# #add_plot( my_circuit.IC_IOUT  )
# ax = plt.gca() 
# ax.set_ylabel('Intensity [A]')
# plt.legend(ylabel)

ax.set_xlabel('Time [s]')
plt.grid(True)
plt.show()