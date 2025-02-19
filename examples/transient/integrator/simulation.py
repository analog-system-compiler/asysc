
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
import integrator
import circuit_base
from integrator import circuit
from circuit_base import circuit_base, element

ylabel = []
def add_plot( element ):
    plt.plot( element.history_x, element.history_y )
    ylabel.append(element.name)

my_circuit = circuit()
my_circuit.simulate_t(0.02,400,1/50,100)

add_plot( my_circuit.V_U  )
add_plot( my_circuit.A_Uout  )
plt.title('Operational Amplifier Integrator simulation example')
plt.ylabel('Voltage [V]')
plt.legend(ylabel)
plt.xlabel('Time [s]')
plt.grid(True)
plt.show()