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
		self.R1_U = element('R1_U')
		self.C1_U = element('C1_U')
		self.L1_U = element('L1_U')
		self.R2_U = element('R2_U')
		self.R1_I = element('R1_I')
		self.VP_I = element('VP_I')
		self.C1_I = element('C1_I')
		self.L1_I = element('L1_I')
		self.R2_I = element('R2_I')
		self.VP_U = element('VP_U')

	def step(self):
		self._setc(self.R1_U,((1e-08*self._der1(self.C1_U))*(0.5*(math.tanh((self._time()-2e-08)/1e-09)-math.tanh(((self._time()-2e-08)-2e-07)/1e-09)))-(1e-08*self._der1(self.C1_U))*(7e-08*self._der0(self.L1_I))+1e-08*self._der0(self.C1_U))/(1e-08*self._der1(self.C1_U)+(1+(1e-08*self._der1(self.C1_U))*(7e-08*self._der1(self.L1_I)))))
		self._setc(self.C1_U,-((7e-08*self._der0(self.L1_I)-0.5*(math.tanh((self._time()-2e-08)/1e-09)-math.tanh(((self._time()-2e-08)-2e-07)/1e-09))+(7e-08*self._der1(self.L1_I)+1)*(1e-08*self._der0(self.C1_U)))/(1+(7e-08*self._der1(self.L1_I)+1)*(1e-08*self._der1(self.C1_U)))))
		self._setc(self.L1_U,((((1e-08*self._der1(self.C1_U))*(7e-08*self._der1(self.L1_I)))*(0.5*(math.tanh((self._time()-2e-08)/1e-09)-math.tanh(((self._time()-2e-08)-2e-07)/1e-09)))+(1e-08*self._der1(self.C1_U)+1)*(7e-08*self._der0(self.L1_I)))+(7e-08*self._der1(self.L1_I))*(1e-08*self._der0(self.C1_U)))/((1e-08*self._der1(self.C1_U))*(7e-08*self._der1(self.L1_I))+(1e-08*self._der1(self.C1_U)+1)))
		self._setc(self.R2_U,0)
		self._setc(self.R1_I,((1e-08*self._der1(self.C1_U))*(0.5*(math.tanh((self._time()-2e-08)/1e-09)-math.tanh(((self._time()-2e-08)-2e-07)/1e-09)))-(1e-08*self._der1(self.C1_U))*(7e-08*self._der0(self.L1_I))+1e-08*self._der0(self.C1_U))/(((1e-08*self._der1(self.C1_U))*(7e-08*self._der1(self.L1_I))+1)+1e-08*self._der1(self.C1_U)))
		self._setc(self.VP_I,-(((1e-08*self._der1(self.C1_U))*(0.5*(math.tanh((self._time()-2e-08)/1e-09)-math.tanh(((self._time()-2e-08)-2e-07)/1e-09)))-(1e-08*self._der1(self.C1_U))*(7e-08*self._der0(self.L1_I))+1e-08*self._der0(self.C1_U))/(((1e-08*self._der1(self.C1_U))*(7e-08*self._der1(self.L1_I))+1)+1e-08*self._der1(self.C1_U))))
		self._setc(self.C1_I,((1e-08*self._der1(self.C1_U))*(0.5*(math.tanh((self._time()-2e-08)/1e-09)-math.tanh(((self._time()-2e-08)-2e-07)/1e-09)))-(1e-08*self._der1(self.C1_U))*(7e-08*self._der0(self.L1_I))+1e-08*self._der0(self.C1_U))/((1e-08*self._der1(self.C1_U)+(1e-08*self._der1(self.C1_U))*(7e-08*self._der1(self.L1_I)))+1))
		self._setc(self.L1_I,(1e-08*self._der0(self.C1_U)-((1e-08*self._der1(self.C1_U))*(7e-08*self._der0(self.L1_I))-(1e-08*self._der1(self.C1_U))*(0.5*(math.tanh((self._time()-2e-08)/1e-09)-math.tanh(((self._time()-2e-08)-2e-07)/1e-09)))))/((1e-08*self._der1(self.C1_U)+1)+(1e-08*self._der1(self.C1_U))*(7e-08*self._der1(self.L1_I))))
		self._setc(self.R2_I,((1e-08*self._der1(self.C1_U))*(0.5*(math.tanh((self._time()-2e-08)/1e-09)-math.tanh(((self._time()-2e-08)-2e-07)/1e-09)))-(1e-08*self._der1(self.C1_U))*(7e-08*self._der0(self.L1_I))+1e-08*self._der0(self.C1_U))/((1e-08*self._der1(self.C1_U)+1)+(1e-08*self._der1(self.C1_U))*(7e-08*self._der1(self.L1_I))))
		self._setc(self.VP_U,(((1e-08*self._der1(self.C1_U)+1)+(1e-08*self._der1(self.C1_U))*(7e-08*self._der1(self.L1_I)))*(0.5*(math.tanh((self._time()-2e-08)/1e-09)-math.tanh(((self._time()-2e-08)-2e-07)/1e-09))))/((1e-08*self._der1(self.C1_U)+1)+(1e-08*self._der1(self.C1_U))*(7e-08*self._der1(self.L1_I))))

