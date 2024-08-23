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
		self.C = element('C')
		self.L = element('L')
		self.R = element('R')
		self.C1_U = element('C1_U')
		self.V_I = element('V_I')
		self.V_U = element('V_U')
		self.R1_U = element('R1_U')
		self.R1_I = element('R1_I')
		self.L1_U = element('L1_U')
		self.L1_I = element('L1_I')
		self.C1_I = element('C1_I')

	def step(self):
		self._setf(self.C1_U,-(1/(self._getv(self.R)*(self._getv(self.C)*self.s)+((self._getv(self.L)*self.s)*(self._getv(self.C)*self.s)+1))), self.freq)
		self._setf(self.V_I,-((self._getv(self.C)*self.s)/(self._getv(self.R)*(self._getv(self.C)*self.s)+((self._getv(self.L)*self.s)*(self._getv(self.C)*self.s)+1))), self.freq)
		self._setf(self.V_U,(((self._getv(self.L)*self.s)*(self._getv(self.C)*self.s)+1)+self._getv(self.R)*(self._getv(self.C)*self.s))/(((self._getv(self.L)*self.s)*(self._getv(self.C)*self.s)+1)+self._getv(self.R)*(self._getv(self.C)*self.s)), self.freq)
		self._setf(self.R1_U,-((self._getv(self.R)*(self._getv(self.C)*self.s))/(self._getv(self.R)*(self._getv(self.C)*self.s)+((self._getv(self.L)*self.s)*(self._getv(self.C)*self.s)+1))), self.freq)
		self._setf(self.R1_I,-((self._getv(self.C)*self.s)/(((self._getv(self.C)*self.s)*self._getv(self.R)+1)+(self._getv(self.L)*self.s)*(self._getv(self.C)*self.s))), self.freq)
		self._setf(self.L1_U,-(((self._getv(self.L)*self.s)*(self._getv(self.C)*self.s))/((self._getv(self.L)*self.s)*(self._getv(self.C)*self.s)+((self._getv(self.C)*self.s)*self._getv(self.R)+1))), self.freq)
		self._setf(self.L1_I,-((self._getv(self.C)*self.s)/(1+(self._getv(self.C)*self.s)*(self._getv(self.R)+self._getv(self.L)*self.s))), self.freq)
		self._setf(self.C1_I,-((self._getv(self.C)*self.s)/((self._getv(self.C)*self.s)*(self._getv(self.R)+self._getv(self.L)*self.s)+1)), self.freq)

