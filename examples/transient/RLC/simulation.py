
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

import matplotlib.pyplot as plt

from matplotlib.widgets import Slider
from RLC import circuit


def main():
    model = circuit()
    model._RV.init(5)
    model.simulate_t(1e-6, 500)

    figure, axis = plt.subplots()
    figure.subplots_adjust(bottom=0.2)
    signals = (model.R1_U, model.C1_U, model.VP_U)
    lines = []
    for signal in signals:
        (line,) = axis.plot(
            signal.history_x, signal.history_y, label=signal.name
        )
        lines.append(line)

    axis.set(
        title="RLC step response",
        xlabel="Time (s)",
        ylabel="Voltage (V)",
    )
    axis.legend()
    axis.grid(True)

    resistance_axis = figure.add_axes([0.1, 0.06, 0.8, 0.03])
    resistance_slider = Slider(
        resistance_axis, label="R", valmin=0, valmax=10, valinit=5
    )

    def update_response(resistance):
        model._RV.init(resistance)
        model.simulate_t(1e-6, 500)
        for line, signal in zip(lines, signals):
            line.set_data(signal.history_x, signal.history_y)
        axis.relim()
        axis.autoscale_view()
        figure.canvas.draw_idle()

    resistance_slider.on_changed(update_response)
    plt.show()


if __name__ == "__main__":
    main()