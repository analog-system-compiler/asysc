
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
    plt.plot(element.history_x, 20 * np.log10(np.absolute(element.history_y)))
    ylabel1.append('gain('+element.name+')')

def add_phase_plot(element):
    plt.plot(element.history_x, np.angle(element.history_y))
    ylabel2.append('phase('+element.name+')')

my_circuit = circuit()
my_circuit.simulate_f(1e5, 1e8, 500)

plt.subplot(2, 1, 1)
plt.title('Sallen-Key filter simulation example')

add_gain_plot(my_circuit.A_Uout)
plt.ylabel("Gain")
plt.xscale('log')
plt.legend(ylabel1)
plt.grid(True, which="both")

plt.subplot(2, 1, 2)
add_phase_plot(my_circuit.A_Uout)
plt.xlabel("Freq (Hz)")
plt.ylabel("Phase")
plt.xscale('log')
plt.legend(ylabel2)
plt.grid(True, which="both")

plt.show()
