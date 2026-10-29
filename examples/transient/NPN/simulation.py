
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

from NPN import circuit


def main():
    # Run a one-second transient to observe transistor bias settling.
    model = circuit()
    model.simulate_t(1, 200, 1 / 20, 50)

    figure, (voltage_axis, current_axis) = plt.subplots(
        2, 1, sharex=True, layout="constrained"
    )
    for signal in (model.BASE_U, model.COLLECTOR_U):
        voltage_axis.plot(signal.history_x, signal.history_y, label=signal.name)
    voltage_axis.set_ylabel("Voltage (V)")
    voltage_axis.set_title("NPN transistor bias")
    voltage_axis.legend()
    voltage_axis.grid(True)

    current_axis.plot(
        model.Q1_IBE.history_x, model.Q1_IBE.history_y, label=model.Q1_IBE.name
    )
    current_axis.set(xlabel="Time (s)", ylabel="Base current (A)")
    current_axis.legend()
    current_axis.grid(True)

    plt.show()


if __name__ == "__main__":
    main()