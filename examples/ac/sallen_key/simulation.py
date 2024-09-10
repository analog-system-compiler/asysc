
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
import sallen_key

from sallen_key import circuit
from circuit_base import circuit_base, element

ylabel1 = []
ylabel2 = []

def add_gain_plot(element):
    axs[0].plot(element.history_x, 20 * np.log10(np.absolute(element.history_y)))
    ylabel1.append('gain('+element.name+')')

def add_phase_plot(element):
    axs[1].plot(element.history_x, np.angle(element.history_y))
    ylabel2.append('phase('+element.name+')')

my_circuit = circuit()
my_circuit.simulate_f(1, 1e7, 500)

fig1, axs = plt.subplots(2, 1, layout="constrained")
add_gain_plot(my_circuit.A_Uout)
add_phase_plot(my_circuit.A_Uout)
axs[1].set_xlabel("Freq (Hz)")
axs[0].set_ylabel("Gain")
axs[1].set_ylabel("Phase")
axs[0].legend(ylabel1)
axs[1].legend(ylabel2)
axs[0].grid(True)
axs[1].grid(True)

plt.show()
