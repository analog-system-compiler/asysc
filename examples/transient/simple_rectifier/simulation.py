
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
import matplotlib.pyplot as plt
import simple_rectifier
import circuit_base
from simple_rectifier import circuit
from circuit_base import circuit_base, element

ylabel = []
def add_plot( element ):
    plt.plot( element.history_x, element.history_y )
    ylabel.append(element.name)

my_circuit = circuit()
my_circuit.simulate_t(0.001,1000,1/50,100)

plt.subplot(1, 1 , 1)
add_plot( my_circuit.V_U  )
add_plot( my_circuit.R_U )
ax = plt.gca()
ax.set_ylabel('Voltage [V]')
ax.set_xlabel('Time [s]')
plt.legend(ylabel)
plt.grid(True)
plt.title('Simple rectifier simulation example')

plt.show()