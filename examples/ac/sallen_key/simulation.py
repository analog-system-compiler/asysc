
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

ylabel = []


def add_gain_plot(axs, element):
    axs.plot(element.history_x, 20 * np.log10(np.absolute(element.history_y)))
    ylabel.append(element.name)


my_circuit = circuit()
my_circuit.simulate_f(1, 1e6, 1000)

fig, axs = plt.subplots(1, 1, layout="constrained")
add_gain_plot(axs, my_circuit.A_Uout)
axs.set_xlabel("Freq (Hz)")
axs.set_ylabel("Gain")
axs.legend(ylabel)
axs.grid(True)

plt.show()
