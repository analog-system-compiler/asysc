#!/usr/bin/python3

# Copyright (C) 2006-2025 The ASysC project
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

from rc_high_pass import circuit


my_circuit = circuit()
my_circuit.simulate_f(10, 1e5, 500)

transfer = np.asarray(my_circuit.OUT_U.history_y) / np.asarray(my_circuit.IN_U.history_y)
frequency = my_circuit.OUT_U.history_x

fig, (gain_axis, phase_axis) = plt.subplots(2, 1, sharex=True)
fig.suptitle("RC high-pass filter (R = 1 kΩ, C = 100 nF)")

gain_axis.plot(frequency, 20 * np.log10(np.abs(transfer)), label="Output")
gain_axis.set_ylabel("Gain (dB)")
gain_axis.grid(True, which="both")
gain_axis.legend()

phase_axis.plot(frequency, np.angle(transfer, deg=True), label="Output")
phase_axis.set_xlabel("Frequency (Hz)")
phase_axis.set_ylabel("Phase (degrees)")
phase_axis.set_xscale("log")
phase_axis.grid(True, which="both")
phase_axis.legend()

plt.show()
