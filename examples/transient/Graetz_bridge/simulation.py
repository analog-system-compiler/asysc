
#!/usr/bin/python3

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

import math
import numpy as np
import matplotlib.pyplot as plt
import graetz_bridge
import circuit_base
from graetz_bridge import circuit
from circuit_base import circuit_base, element


def add_plot( element ):
    plt.plot( element.history_x, element.history_y )
    ylabel.append(element.name)

my_circuit = circuit()
my_circuit.simulate_t(1e-3,500,1/10,100)

plt.subplot(2, 1, 1)
ylabel = []
add_plot( my_circuit.V_U )
add_plot( my_circuit.R1_U )
add_plot( my_circuit.D3_U )
add_plot( my_circuit.D4_U )
ax = plt.gca()
ax.set_ylabel('Voltage [V]')
plt.legend(ylabel)
plt.grid(True)

plt.subplot(2, 1, 2)
ylabel = []
add_plot( my_circuit.R2_I )
ax = plt.gca()
ax.set_xlabel('Time [s]')
ax.set_ylabel('Intensity [A]')
plt.legend(ylabel)
plt.grid(True)

plt.show()