
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
import div4
import circuit_base
from div4 import circuit
from circuit_base import circuit_base, element

ylabel = []
def add_plot( axs, element ):
    axs.plot( element.history_x, element.history_y )
    axs.legend(element.name)

my_circuit = circuit()
my_circuit.simulate_t(0.001,512)

fig, axs = plt.subplots(3, 1, layout='constrained')
add_plot( axs[0], my_circuit.V_U )
add_plot( axs[1], my_circuit.FF0_Uout )
add_plot( axs[2], my_circuit.FF1_Uout )
axs[1].set_xlabel('Time (s)')
axs[0].grid(True)
axs[1].grid(True)

plt.show()