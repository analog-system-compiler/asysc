
#!/usr/bin/python3

# Copyright (C) 2006-2026 The ASysC project
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

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.widgets import Slider
from RLC import circuit


def main():
    model = circuit()
    model.R.init(5)
    model.C.init(1e-5)
    model.L.init(1e-5)

    # Recompute the frequency response whenever any component slider changes.
    model.simulate_f(10, 1e6, 100)
    frequency = model.R1_U.history_x
    figure, axis = plt.subplots()
    figure.subplots_adjust(bottom=0.28)
    axis.set(
        title="RLC filter response",
        xlabel="Frequency (Hz)",
        ylabel="Gain (dB)",
    )
    axis.set_xscale("log")
    axis.grid(True, which="both")

    signals = (model.R1_U, model.C1_U, model.L1_U)
    lines = []
    for signal in signals:
        gain_db = 20 * np.log10(np.abs(signal.history_y))
        (line,) = axis.plot(frequency, gain_db, label=signal.name)
        lines.append(line)
    axis.legend()

    resistance_axis = figure.add_axes([0.15, 0.16, 0.7, 0.03])
    capacitance_axis = figure.add_axes([0.15, 0.10, 0.7, 0.03])
    inductance_axis = figure.add_axes([0.15, 0.04, 0.7, 0.03])
    resistance_slider = Slider(
        resistance_axis, "R", valmin=1, valmax=10, valinit=5
    )
    capacitance_slider = Slider(
        capacitance_axis, "C (F)", valmin=1e-6, valmax=1e-4, valinit=1e-5
    )
    inductance_slider = Slider(
        inductance_axis, "L (H)", valmin=1e-6, valmax=1e-4, valinit=1e-5
    )

    def update_response(_value):
        model.R.init(resistance_slider.val)
        model.C.init(capacitance_slider.val)
        model.L.init(inductance_slider.val)
        model.simulate_f(10, 1e6, 100)

        for line, signal in zip(lines, signals):
            line.set_data(
                signal.history_x,
                20 * np.log10(np.abs(signal.history_y)),
            )

        axis.relim()
        axis.autoscale_view()
        figure.canvas.draw_idle()

    resistance_slider.on_changed(update_response)
    capacitance_slider.on_changed(update_response)
    inductance_slider.on_changed(update_response)
    plt.show()


if __name__ == "__main__":
    main()
