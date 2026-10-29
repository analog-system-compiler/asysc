
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

from delay_line import circuit


def main():
    # A short run captures the signal propagation and reflected wave.
    model = circuit()
    model.simulate_t(2e-7, 300)

    figure, axis = plt.subplots(layout="constrained")
    for signal in (model.R1_U, model.VP_U):
        axis.plot(signal.history_x, signal.history_y, label=signal.name)

    axis.set(
        title="Delay line and impedance mismatch",
        xlabel="Time (s)",
        ylabel="Voltage (V)",
    )
    axis.legend()
    axis.grid(True)
    plt.show()


if __name__ == "__main__":
    main()