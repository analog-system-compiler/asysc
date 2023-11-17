
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
    ylabel.append(element.name)
    return axs.plot(element.history_x, 20 * np.log10(np.absolute(element.history_y)))    

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
    global lineR, lineC, lineL
    my_circuit.simulate_f(1, 1e6, 100)    
    if first_time:
        lineR, =add_gain_plot(axs, my_circuit.R_U)
        lineC, =add_gain_plot(axs, my_circuit.C_U)
        lineL, =add_gain_plot(axs, my_circuit.L_U)
        axs.set_xlabel("Freq (Hz)")
        axs.set_ylabel("Gain")
        axs.legend(ylabel)
        axs.grid(True)
        axs.set_xscale('log')
        first_time = False
    else:
        lineR.set_ydata(20 * np.log10(np.absolute(my_circuit.R_U.history_y)))
        lineL.set_ydata(20 * np.log10(np.absolute(my_circuit.L_U.history_y)))
        lineC.set_ydata(20 * np.log10(np.absolute(my_circuit.C_U.history_y)))
        fig.canvas.draw_idle()       

my_circuit = circuit()

#plt.ion()
fig, axs = plt.subplots(1, 1, layout="constrained")
plt.subplots_adjust(bottom=0.25)
r_axe= plt.axes([0.25, 0.0, 0.65, 0.03])
l_axe= plt.axes([0.25, 0.04, 0.65, 0.03])
c_axe= plt.axes([0.25, 0.08, 0.65, 0.03])
r_slider = Slider(ax=r_axe, label='R', valmin=1,    valmax=10,   valinit=5)
c_slider = Slider(ax=l_axe, label='C', valmin=1e-6, valmax=1e-4, valinit=1e-5)
l_slider = Slider(ax=c_axe, label='L', valmin=1e-6, valmax=1e-4, valinit=1e-5)
my_circuit.R.set_t( 5 )
my_circuit.C.set_t(1e-5)
my_circuit.L.set_t(1e-5)
r_slider.on_changed(update_R)
c_slider.on_changed(update_C)
l_slider.on_changed(update_L)
update_all()
plt.show()

