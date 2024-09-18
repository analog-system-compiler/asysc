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
import NE555
import circuit_base
from matplotlib.widgets import Slider
from NE555 import circuit
from circuit_base import circuit_base, element

ylabel = []
first_time = True

def update_R(val):    
    global first_time, ylabel
    global fig, axs
    global UTRESH, UOUT
    fig.canvas.draw_idle()
    my_circuit._setc(my_circuit._RV, val)
    my_circuit.simulate_t(0.1, 200)
    if first_time:
        ylabel.append(my_circuit.IC_UTRESH.name)
        ylabel.append(my_circuit.IC_UOUT.name)        
        (UTRESH,) = axs.plot(
            my_circuit.IC_UTRESH.history_x, my_circuit.IC_UTRESH.history_y
        )
        (UOUT,) = axs.plot(my_circuit.IC_UOUT.history_x, my_circuit.IC_UOUT.history_y)
        axs.legend(ylabel)
        first_time = False
    else:
        UTRESH.set_ydata(my_circuit.IC_UTRESH.history_y)
        UOUT.set_ydata(my_circuit.IC_UOUT.history_y)
        fig.canvas.draw_idle()

my_circuit = circuit()

fig, axs = plt.subplots()
fig.subplots_adjust(bottom=0.22)
axs.set_xlabel("Time [s]")
axs.set_ylabel("Voltage [V]")
plt.grid(True)

r_axe = plt.axes([0.2, 0.1, 0.65, 0.03])
r_slider = Slider(ax=r_axe, label="R", valmin=2000, valmax=50000, valinit=13000)
r_slider.on_changed(update_R)
update_R(13000)

plt.show()
