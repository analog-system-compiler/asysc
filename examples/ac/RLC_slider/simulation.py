
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
#from circuit_base import circuit_base, element

ylabel = []
first_time = True

def add_gain_plot(axs, element):
    ylabel.append(element.name)
    return axs.plot(element.history_x, 20 * np.log10(np.absolute(element.history_y)))    

def update_R(val):
    my_circuit._setc(my_circuit.R, val )
    update_all()

def update_L(val):
    my_circuit._setc(my_circuit.L, val )
    update_all()

def update_C(val):
    my_circuit._setc(my_circuit.C, val )
    update_all()    

def update_all():    
    global first_time, axs
    global lineR, lineC, lineL
    my_circuit.simulate_f(1, 1e6, 100)    
    if first_time:
        lineR, =add_gain_plot(axs, my_circuit.R1_U)
        lineC, =add_gain_plot(axs, my_circuit.C1_U)
        lineL, =add_gain_plot(axs, my_circuit.L1_U)
        axs.set_xlabel("Freq (Hz)")
        axs.set_ylabel("Gain")
        axs.legend(ylabel)
        axs.grid(True)
        axs.set_xscale('log')
        first_time = False
    else:
        lineR.set_ydata(20 * np.log10(np.absolute(my_circuit.R1_U.history_y)))
        lineL.set_ydata(20 * np.log10(np.absolute(my_circuit.L1_U.history_y)))
        lineC.set_ydata(20 * np.log10(np.absolute(my_circuit.C1_U.history_y)))
        fig.canvas.draw_idle()       

my_circuit = circuit()

#plt.ion()
fig, axs = plt.subplots()
fig.subplots_adjust(bottom=0.22)
r_axe= plt.axes([0.1, 0.0, 0.65, 0.03])
l_axe= plt.axes([0.1, 0.04, 0.65, 0.03])
c_axe= plt.axes([0.1, 0.08, 0.65, 0.03])
r_slider = Slider(ax=r_axe, label='R', valmin=1,    valmax=10,   valinit=5)
c_slider = Slider(ax=l_axe, label='C', valmin=1e-6, valmax=1e-4, valinit=1e-5)
l_slider = Slider(ax=c_axe, label='L', valmin=1e-6, valmax=1e-4, valinit=1e-5)
my_circuit._setc(my_circuit.R, 5 )
my_circuit._setc(my_circuit.C,1e-5)
my_circuit._setc(my_circuit.L,1e-5)
r_slider.on_changed(update_R)
c_slider.on_changed(update_C)
l_slider.on_changed(update_L)
update_all()
plt.show()

