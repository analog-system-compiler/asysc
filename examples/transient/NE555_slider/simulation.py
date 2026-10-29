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

import matplotlib.pyplot as plt

from matplotlib.widgets import Slider
from NE555 import circuit


def main():
    model = circuit()
    figure, axis = plt.subplots()
    figure.subplots_adjust(bottom=0.22)
    axis.set(
        title="NE555 oscillator",
        xlabel="Time (s)",
        ylabel="Voltage (V)",
    )
    axis.grid(True)

    # Adjust the timing resistance and redraw both oscillator node voltages.
    model._RV.init(13000)
    model.simulate_t(0.1, 200)
    signals = (model.U_UTRESH, model.U_UOUT)
    lines = []
    for signal in signals:
        (line,) = axis.plot(
            signal.history_x, signal.history_y, label=signal.name
        )
        lines.append(line)
    axis.legend()

    resistance_axis = figure.add_axes([0.2, 0.1, 0.65, 0.03])
    resistance_slider = Slider(
        ax=resistance_axis,
        label="R (Ω)",
        valmin=2000,
        valmax=50000,
        valinit=13000,
    )

    def update_resistance(resistance):
        model._RV.init(resistance)
        model.simulate_t(0.1, 200)
        for line, signal in zip(lines, signals):
            line.set_data(signal.history_x, signal.history_y)
        axis.relim()
        axis.autoscale_view()
        figure.canvas.draw_idle()

    resistance_slider.on_changed(update_resistance)
    plt.show()


if __name__ == "__main__":
    main()
