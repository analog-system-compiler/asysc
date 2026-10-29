
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

from oscillator import circuit


def main():
    model = circuit()
    # Set an initial logic level so the feedback oscillator starts switching.
    model.NOT1_Uin.init(5)
    model.simulate_t(0.01, 512)

    figure, axis = plt.subplots(layout="constrained")
    for signal in (model.NOT1_Uin, model.NOT1_Uout):
        axis.plot(signal.history_x, signal.history_y, label=signal.name)

    axis.set(title="NOT-gate oscillator", xlabel="Time (s)", ylabel="Voltage (V)")
    axis.legend()
    axis.grid(True)
    plt.show()


if __name__ == "__main__":
    main()