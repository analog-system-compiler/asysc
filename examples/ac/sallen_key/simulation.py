
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

import numpy as np
import matplotlib.pyplot as plt

from sallen_key import circuit


def main():
    model = circuit()
    model.simulate_f(1e5, 1e8, 500)

    frequency = model.A_Uout.history_x
    response = np.asarray(model.A_Uout.history_y)

    figure, (gain_axis, phase_axis) = plt.subplots(2, 1, sharex=True)
    figure.suptitle("Sallen-Key filter")

    gain_axis.plot(
        frequency,
        20 * np.log10(np.abs(response)),
        label=f"Gain ({model.A_Uout.name})",
    )
    gain_axis.set_ylabel("Gain (dB)")
    gain_axis.set_xscale("log")
    gain_axis.legend()
    gain_axis.grid(True, which="both")

    # Express phase in degrees to match the usual filter-response convention.
    phase_axis.plot(
        frequency,
        np.angle(response, deg=True),
        label=f"Phase ({model.A_Uout.name})",
    )
    phase_axis.set(xlabel="Frequency (Hz)", ylabel="Phase (degrees)")
    phase_axis.set_xscale("log")
    phase_axis.legend()
    phase_axis.grid(True, which="both")

    plt.show()


if __name__ == "__main__":
    main()
