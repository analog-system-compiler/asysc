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

import matplotlib.pyplot as plt

from envelope_detector import circuit


my_circuit = circuit()
my_circuit.simulate_t(0.02, 500, 1 / 50, 100)

plt.plot(my_circuit.IN_U.history_x, my_circuit.IN_U.history_y, label="Input")
plt.plot(my_circuit.OUT_U.history_x, my_circuit.OUT_U.history_y, label="Detected envelope")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Diode RC envelope detector (1 kHz, R = 100 kΩ, C = 100 nF)")
plt.grid(True)
plt.legend()
plt.show()
