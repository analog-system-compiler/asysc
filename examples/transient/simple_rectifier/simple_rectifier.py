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
		self.R2_U = element('R2_U')
		self.D1_U = element('D1_U')
		self.D1_I = element('D1_I')
		self.V_I = element('V_I')
		self.R2_I = element('R2_I')
		self.V_U = element('V_U')

	def step(self):
		self._setc(self.R2_U,(((1e-15*math.exp(self._last(self.D1_U)/0.026))*(5*math.sin(23687.0505626*self._time())))/0.026-1e-15*((1-self._last(self.D1_U)/0.026)*math.exp(self._last(self.D1_U)/0.026)-1))/((1e-15*math.exp(self._last(self.D1_U)/0.026))/0.026+1))
		self._setc(self.D1_U,-((1e-15*((1-self._last(self.D1_U)/0.026)*math.exp(self._last(self.D1_U)/0.026)-1)+5*math.sin(23687.0505626*self._time()))/(1+(1e-15*math.exp(self._last(self.D1_U)/0.026))/0.026)))
		self._setc(self.D1_I,(1e-15*((1-self._last(self.D1_U)/0.026)*math.exp(self._last(self.D1_U)/0.026)-1)-((1e-15*math.exp(self._last(self.D1_U)/0.026))*(5*math.sin(23687.0505626*self._time())))/0.026)/((1e-15*math.exp(self._last(self.D1_U)/0.026))/0.026+1))
		self._setc(self.V_I,(1e-15*((1-self._last(self.D1_U)/0.026)*math.exp(self._last(self.D1_U)/0.026)-1)-((1e-15*math.exp(self._last(self.D1_U)/0.026))*(5*math.sin(23687.0505626*self._time())))/0.026)/(1+(1e-15*math.exp(self._last(self.D1_U)/0.026))/0.026))
		self._setc(self.R2_I,(((1e-15*math.exp(self._last(self.D1_U)/0.026))*(5*math.sin(23687.0505626*self._time())))/0.026-1e-15*((1-self._last(self.D1_U)/0.026)*math.exp(self._last(self.D1_U)/0.026)-1))/(1+(1e-15*math.exp(self._last(self.D1_U)/0.026))/0.026))
		self._setc(self.V_U,(((1e-15*math.exp(self._last(self.D1_U)/0.026))/0.026+1)*(5*math.sin(23687.0505626*self._time())))/((1e-15*math.exp(self._last(self.D1_U)/0.026))/0.026+1))

