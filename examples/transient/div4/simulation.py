
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

from div4 import circuit


def main():
    # Simulate one millisecond to show the input and both divider stages.
    model = circuit()
    model.simulate_t(0.001, 512)

    figure, axes = plt.subplots(3, 1, sharex=True, layout="constrained")
    figure.suptitle("Divider-by-4 digital simulation")
    signals = (model.V2_U, model.FF0_Uout, model.FF1_Uout)
    for axis, signal in zip(axes, signals):
        axis.plot(signal.history_x, signal.history_y, label=signal.name)
        axis.set_ylabel("Voltage (V)")
        axis.legend()
        axis.grid(True)

    axes[-1].set_xlabel("Time (s)")
    plt.show()


if __name__ == "__main__":
    main()