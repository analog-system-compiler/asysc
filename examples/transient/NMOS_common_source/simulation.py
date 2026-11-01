#!/usr/bin/python3

# Copyright (C) 2006-2026 The ASysC project
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <https://www.gnu.org/licenses/>

import matplotlib.pyplot as plt

from NMOS_common_source import circuit


def main():
    model = circuit()
    model.simulate_t(0.005, 500, 1 / 100, 100)

    figure, (input_axis, output_axis) = plt.subplots(
        2, 1, sharex=True, layout="constrained"
    )
    input_axis.plot(model.IN_U.history_x, model.IN_U.history_y)
    input_axis.set_ylabel("Gate voltage (V)")
    input_axis.set_title("NMOS common-source amplifier")
    input_axis.grid(True)

    output_axis.plot(model.OUT_U.history_x, model.OUT_U.history_y)
    output_axis.set(xlabel="Time (s)", ylabel="Drain voltage (V)")
    output_axis.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
