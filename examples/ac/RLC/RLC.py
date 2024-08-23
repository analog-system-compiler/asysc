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
		self.C_U = element('C_U')
		self.V_I = element('V_I')
		self.V_U = element('V_U')
		self.R_U = element('R_U')
		self.R_I = element('R_I')
		self.L_U = element('L_U')
		self.L_I = element('L_I')
		self.C_I = element('C_I')

	def step(self):
		self._setf(self.C_U,-(1/(100*(1e-05*self.s)+((0.001*self.s)*(1e-05*self.s)+1))), self.freq)
		self._setf(self.V_I,-((1e-05*self.s)/(100*(1e-05*self.s)+((0.001*self.s)*(1e-05*self.s)+1))), self.freq)
		self._setf(self.V_U,(((0.001*self.s)*(1e-05*self.s)+1)+100*(1e-05*self.s))/(((0.001*self.s)*(1e-05*self.s)+1)+100*(1e-05*self.s)), self.freq)
		self._setf(self.R_U,-((100*(1e-05*self.s))/(100*(1e-05*self.s)+((0.001*self.s)*(1e-05*self.s)+1))), self.freq)
		self._setf(self.R_I,-((1e-05*self.s)/(((1e-05*self.s)*100+1)+(0.001*self.s)*(1e-05*self.s))), self.freq)
		self._setf(self.L_U,-(((0.001*self.s)*(1e-05*self.s))/((0.001*self.s)*(1e-05*self.s)+((1e-05*self.s)*100+1))), self.freq)
		self._setf(self.L_I,-((1e-05*self.s)/(1+(1e-05*self.s)*(100+0.001*self.s))), self.freq)
		self._setf(self.C_I,-((1e-05*self.s)/((1e-05*self.s)*(100+0.001*self.s)+1)), self.freq)

