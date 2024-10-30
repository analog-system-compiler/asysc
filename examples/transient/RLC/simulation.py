
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
import circuit_base

from matplotlib.widgets import Slider
from RLC import circuit
from circuit_base import circuit_base, element

ylabel = []

def add_plot( axs, element ):
    axs.plot( element.history_x, element.history_y )
    ylabel.append(element.name)

def update_R(val):
    my_circuit._RV.init( val )
    update_all()

def update_all():    
    my_circuit.simulate_t(1e-6, 500)
    axs.cla()  
    add_plot( axs, my_circuit.R1_U )
    add_plot( axs, my_circuit.C1_U )
    add_plot( axs, my_circuit.VP_U )
    axs.set_xlabel('Time (s)')
    axs.set_ylabel('Voltage (V)')
    axs.legend(ylabel)
    axs.grid(True)

my_circuit = circuit()

fig, axs = plt.subplots()
fig.subplots_adjust(bottom=0.20)
r_axe = plt.axes([0.1, 0.06, 0.80, 0.03])
r_slider = Slider(ax=r_axe, label='R', valmin=0, valmax=10, valinit=5)
r_slider.on_changed(update_R)
my_circuit._RV.init( 5 )
update_all()

plt.show()