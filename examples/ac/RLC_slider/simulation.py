
#!/usr/bin/python3

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
    axs.plot(element.history_x, 20 * np.log10(np.absolute(element.history_y)))
    ylabel.append(element.name)

def update_R(val):
    my_circuit.R.set_t( val )
    update_all()

def update_L(val):
    my_circuit.L.set_t( val )
    update_all()

def update_C(val):
    my_circuit.C.set_t( val )
    update_all()    

def update_all():    
    global first_time
    my_circuit.simulate_f(1, 1e6, 100)    
    if first_time:
        add_gain_plot(axs, my_circuit.R_U)
        add_gain_plot(axs, my_circuit.C_U)
        add_gain_plot(axs, my_circuit.L_U)
        axs.set_xlabel("Freq (Hz)")
        axs.set_ylabel("Gain")
        axs.legend(ylabel)
        axs.grid(True)
        axs.set_xscale('log')
    else:
        axs.lines[0].set_ydata(20 * np.log10(np.absolute(my_circuit.R_U.history_y)))
        axs.lines[1].set_ydata(20 * np.log10(np.absolute(my_circuit.L_U.history_y)))
        axs.lines[2].set_ydata(20 * np.log10(np.absolute(my_circuit.C_U.history_y)))
    first_time = False
    fig.canvas.draw()
    fig.canvas.flush_events()
    
my_circuit = circuit()

#plt.ion()
fig, axs = plt.subplots(1, 1, layout="constrained")
plt.subplots_adjust(bottom=0.25)
r_axe= plt.axes([0.25, 0.0, 0.65, 0.03])
l_axe= plt.axes([0.25, 0.04, 0.65, 0.03])
c_axe= plt.axes([0.25, 0.08, 0.65, 0.03])
r_slider = Slider(r_axe, 'R', 1, 10, 5)
c_slider = Slider(l_axe, 'C', 1e-6, 1e-4, 1e-5)
l_slider = Slider(c_axe, 'L', 1e-6, 1e-4, 1e-5)
r_slider.on_changed(update_R)
c_slider.on_changed(update_C)
l_slider.on_changed(update_L)
update_all()
plt.show()
