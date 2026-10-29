
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

from graetz_bridge import circuit


def main():
    # Capture the bridge's input/output voltages and load current.
    model = circuit()
    model.simulate_t(1e-3, 500, 1 / 10, 100)

    figure, (voltage_axis, current_axis) = plt.subplots(
        2, 1, sharex=True, layout="constrained"
    )
    for signal in (model.V_U, model.R1_U):
        voltage_axis.plot(signal.history_x, signal.history_y, label=signal.name)
    voltage_axis.set_ylabel("Voltage (V)")
    voltage_axis.set_title("Graetz bridge")
    voltage_axis.legend()
    voltage_axis.grid(True)

    current_axis.plot(
        model.R2_I.history_x, model.R2_I.history_y, label=model.R2_I.name
    )
    current_axis.set(xlabel="Time (s)", ylabel="Current (A)")
    current_axis.legend()
    current_axis.grid(True, which="both")

    plt.show()


if __name__ == "__main__":
    main()