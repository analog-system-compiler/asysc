
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
import RLC

from matplotlib.widgets import Slider
from RLC import circuit

ylabel = []
first_time = True

def add_gain_plot(axs, element):
    global ylabel
    ylabel.append(element.name)
    return axs.plot(element.history_x, 20 * np.log10(np.absolute(element.history_y)))    

def update_R(val):
    my_circuit.R.init( val )
    update_all()

def update_L(val):
    my_circuit.L.init( val )
    update_all()

def update_C(val):
    my_circuit.C.init( val )
    update_all()    

def update_all():    
    global first_time, axs, fig
    global lineR, lineC, lineL
    my_circuit.simulate_f(10, 1e6, 100)    
    if first_time:
        lineR, =add_gain_plot(axs, my_circuit.R1_U)
        lineC, =add_gain_plot(axs, my_circuit.C1_U)
        lineL, =add_gain_plot(axs, my_circuit.L1_U)        
        first_time = False
    else:
        lineR.set_ydata(20 * np.log10(np.absolute(my_circuit.R1_U.history_y)))
        lineL.set_ydata(20 * np.log10(np.absolute(my_circuit.L1_U.history_y)))
        lineC.set_ydata(20 * np.log10(np.absolute(my_circuit.C1_U.history_y)))
        fig.canvas.draw_idle()

my_circuit = circuit()

fig, axs = plt.subplots()
plt.title('RLC filter simulation example')
fig.subplots_adjust(bottom=0.22)
r_axe= plt.axes([0.1, 0.0, 0.65, 0.03])
l_axe= plt.axes([0.1, 0.04, 0.65, 0.03])
c_axe= plt.axes([0.1, 0.08, 0.65, 0.03])
r_slider = Slider(ax=r_axe, label='R', valmin=1,    valmax=10,   valinit=5)
c_slider = Slider(ax=l_axe, label='C', valmin=1e-6, valmax=1e-4, valinit=1e-5)
l_slider = Slider(ax=c_axe, label='L', valmin=1e-6, valmax=1e-4, valinit=1e-5)
my_circuit.R.init( 5 )
my_circuit.C.init( 1e-5)
my_circuit.L.init( 1e-5)
axs.set_xlabel("Freq (Hz)")
axs.set_ylabel("Gain")
axs.grid(True, which="both")
axs.set_xscale('log')
r_slider.on_changed(update_R)
c_slider.on_changed(update_C)
l_slider.on_changed(update_L)
update_all()
axs.legend(ylabel)
plt.show()

