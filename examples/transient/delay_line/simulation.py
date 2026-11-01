
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
from delay_line import circuit


def main():
    model = circuit()
    model._RL.init(100)
    model.simulate_t(2e-7, 300)

    figure, axis = plt.subplots()
    figure.subplots_adjust(bottom=0.2)
    signals = (model.R1_U, model.VP_U)
    lines = []
    for signal in signals:
        (line,) = axis.plot(signal.history_x, signal.history_y, label=signal.name)
        lines.append(line)

    axis.set(
        title="Delay line and impedance mismatch",
        xlabel="Time (s)",
        ylabel="Voltage (V)",
    )
    axis.legend()
    axis.grid(True)

    impedance_axis = figure.add_axes([0.15, 0.06, 0.7, 0.03])
    impedance_slider = Slider(
        impedance_axis,
        label="Load impedance (Ω)",
        valmin=10,
        valmax=200,
        valinit=100,
    )

    def update_response(impedance):
        model._RL.init(impedance)
        model.simulate_t(2e-7, 300)
        for line, signal in zip(lines, signals):
            line.set_data(signal.history_x, signal.history_y)
        axis.relim()
        axis.autoscale_view()
        figure.canvas.draw_idle()

    impedance_slider.on_changed(update_response)
    plt.show()


if __name__ == "__main__":
    main()