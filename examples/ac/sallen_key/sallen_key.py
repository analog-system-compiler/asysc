# Copyright (C) 2006-2024 The ASysC project                        
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

import math
import circuit_base
from circuit_base import circuit_base, element

class circuit( circuit_base ):

	def __init__(self):
		super().__init__()
		self.A_Uin = element('A_Uin')
		self.V_I = element('V_I')
		self.A_Iout = element('A_Iout')
		self.V_U = element('V_U')
		self.R1_U = element('R1_U')
		self.R1_I = element('R1_I')
		self.R2_I = element('R2_I')
		self.R2_U = element('R2_U')
		self.C1_I = element('C1_I')
		self.C1_U = element('C1_U')
		self.C2_I = element('C2_I')
		self.A_Uout = element('A_Uout')
		self.C2_U = element('C2_U')
		self.A_Iin = element('A_Iin')

	def step(self):
		self._setf(self.A_Uin,0, self.freq)
		self._setf(self.V_I,-((3.9e-10*self.s+100*((8.2e-10*self.s)*(3.9e-10*self.s)))/(100*(3.9e-10*self.s+100*((8.2e-10*self.s)*(3.9e-10*self.s)))+(1+100*(3.9e-10*self.s)))), self.freq)
		self._setf(self.A_Iout,(100*((8.2e-10*self.s)*(3.9e-10*self.s)))/(100*(3.9e-10*self.s+100*((8.2e-10*self.s)*(3.9e-10*self.s)))+(1+100*(3.9e-10*self.s))), self.freq)
		self._setf(self.V_U,((1+100*(3.9e-10*self.s))+100*(3.9e-10*self.s+100*((8.2e-10*self.s)*(3.9e-10*self.s))))/((1+100*(3.9e-10*self.s))+100*(3.9e-10*self.s+100*((8.2e-10*self.s)*(3.9e-10*self.s)))), self.freq)
		self._setf(self.R1_U,(100*(3.9e-10*self.s+100*((8.2e-10*self.s)*(3.9e-10*self.s))))/(100*(3.9e-10*self.s+100*((8.2e-10*self.s)*(3.9e-10*self.s)))+(1+100*(3.9e-10*self.s))), self.freq)
		self._setf(self.R1_I,(100*((8.2e-10*self.s)*(3.9e-10*self.s))+3.9e-10*self.s)/(100*((8.2e-10*self.s)*((3.9e-10*self.s)*100)+3.9e-10*self.s)+((3.9e-10*self.s)*100+1)), self.freq)
		self._setf(self.R2_I,(3.9e-10*self.s)/(((8.2e-10*self.s)*((3.9e-10*self.s)*10000)+(3.9e-10*self.s)*100)+((3.9e-10*self.s)*100+1)), self.freq)
		self._setf(self.R2_U,((3.9e-10*self.s)*100)/((((3.9e-10*self.s)*100+1)+(3.9e-10*self.s)*100)+(8.2e-10*self.s)*((3.9e-10*self.s)*10000)), self.freq)
		self._setf(self.C1_I,((8.2e-10*self.s)*((3.9e-10*self.s)*100))/((8.2e-10*self.s)*((3.9e-10*self.s)*10000)+(((3.9e-10*self.s)*100+1)+(3.9e-10*self.s)*100)), self.freq)
		self._setf(self.C1_U,((3.9e-10*self.s)*100)/(1+(3.9e-10*self.s)*(100*(1+100*(8.2e-10*self.s))+100)), self.freq)
		self._setf(self.C2_I,(3.9e-10*self.s)/((3.9e-10*self.s)*(100*(1+100*(8.2e-10*self.s))+100)+1), self.freq)
		self._setf(self.A_Uout,1/(1+(3.9e-10*self.s)*(100*(1+100*(8.2e-10*self.s))+100)), self.freq)
		self._setf(self.C2_U,1/(100*(3.9e-10*self.s+100*((8.2e-10*self.s)*(3.9e-10*self.s)))+(1+100*(3.9e-10*self.s))), self.freq)
		self._setf(self.A_Iin,0, self.freq)

