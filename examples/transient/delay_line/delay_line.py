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
		self.DL1_U1 = element('DL1_U1')
		self.L1_U = element('L1_U')
		self.R2_U = element('R2_U')
		self.R3_I = element('R3_I')
		self.DL2_I2 = element('DL2_I2')
		self.DL2_I1 = element('DL2_I1')
		self.R1_I = element('R1_I')
		self.DL1_I2 = element('DL1_I2')
		self.DL1_I1 = element('DL1_I1')
		self.C1_I = element('C1_I')
		self.VP_I = element('VP_I')
		self.L1_I = element('L1_I')
		self.R2_I = element('R2_I')
		self.C1_U = element('C1_U')
		self.DL1_A = element('DL1_A')
		self.DL1_U2 = element('DL1_U2')
		self.DL2_U1 = element('DL2_U1')
		self.R1_U = element('R1_U')
		self.DL2_A = element('DL2_A')
		self.DL2_U2 = element('DL2_U2')
		self.R3_U = element('R3_U')
		self.VP_U = element('VP_U')

	def step(self):
		self._setc(self.DL1_U1,(28125000*(0.5*(math.tanh((self._time()-1e-08)/1e-09)-math.tanh(((self._time()-1e-08)-8e-08)/1e-09)))+(self._delay(self.DL1_U2,1e-08)+50*self._delay(self.DL1_I2,1e-08))*28125000)/56250000)
		self._setc(self.L1_U,0)
		self._setc(self.R2_U,(28125000*(0.5*(math.tanh((self._time()-1e-08)/1e-09)-math.tanh(((self._time()-1e-08)-8e-08)/1e-09)))-(self._delay(self.DL1_U2,1e-08)+50*self._delay(self.DL1_I2,1e-08))*28125000)/56250000)
		self._setc(self.R3_I,((self._delay(self.DL2_U1,1e-08)+50*self._delay(self.DL2_I1,1e-08))*250000+50*((self._delay(self.DL2_U1,1e-08)+50*self._delay(self.DL2_I1,1e-08))*10000))/56250000)
		self._setc(self.DL2_I2,-(((self._delay(self.DL2_U1,1e-08)+50*self._delay(self.DL2_I1,1e-08))*250000+50*((self._delay(self.DL2_U1,1e-08)+50*self._delay(self.DL2_I1,1e-08))*10000))/56250000))
		self._setc(self.DL2_I1,(((self._delay(self.DL1_U1,1e-08)+50*self._delay(self.DL1_I1,1e-08))*187500+50*((self._delay(self.DL1_U1,1e-08)+50*self._delay(self.DL1_I1,1e-08))*3750))-(self._delay(self.DL2_U2,1e-08)+50*self._delay(self.DL2_I2,1e-08))*750000)/56250000)
		self._setc(self.R1_I,(((self._delay(self.DL1_U1,1e-08)+50*self._delay(self.DL1_I1,1e-08))*187500+50*((self._delay(self.DL1_U1,1e-08)+50*self._delay(self.DL1_I1,1e-08))*3750))+(self._delay(self.DL2_U2,1e-08)+50*self._delay(self.DL2_I2,1e-08))*375000)/56250000)
		self._setc(self.DL1_I2,((self._delay(self.DL2_U2,1e-08)+50*self._delay(self.DL2_I2,1e-08))*375000-((self._delay(self.DL1_U1,1e-08)+50*self._delay(self.DL1_I1,1e-08))*375000+50*((self._delay(self.DL1_U1,1e-08)+50*self._delay(self.DL1_I1,1e-08))*7500)))/56250000)
		self._setc(self.DL1_I1,(562500*(0.5*(math.tanh((self._time()-1e-08)/1e-09)-math.tanh(((self._time()-1e-08)-8e-08)/1e-09)))-(self._delay(self.DL1_U2,1e-08)+50*self._delay(self.DL1_I2,1e-08))*562500)/56250000)
		self._setc(self.C1_I,0)
		self._setc(self.VP_I,((self._delay(self.DL1_U2,1e-08)+50*self._delay(self.DL1_I2,1e-08))*562500-562500*(0.5*(math.tanh((self._time()-1e-08)/1e-09)-math.tanh(((self._time()-1e-08)-8e-08)/1e-09))))/56250000)
		self._setc(self.L1_I,(562500*(0.5*(math.tanh((self._time()-1e-08)/1e-09)-math.tanh(((self._time()-1e-08)-8e-08)/1e-09)))-(self._delay(self.DL1_U2,1e-08)+50*self._delay(self.DL1_I2,1e-08))*562500)/56250000)
		self._setc(self.R2_I,(562500*(0.5*(math.tanh((self._time()-1e-08)/1e-09)-math.tanh(((self._time()-1e-08)-8e-08)/1e-09)))-(self._delay(self.DL1_U2,1e-08)+50*self._delay(self.DL1_I2,1e-08))*562500)/56250000)
		self._setc(self.C1_U,(28125000*(0.5*(math.tanh((self._time()-1e-08)/1e-09)-math.tanh(((self._time()-1e-08)-8e-08)/1e-09)))+(self._delay(self.DL1_U2,1e-08)+50*self._delay(self.DL1_I2,1e-08))*28125000)/56250000)
		self._setc(self.DL1_A,1)
		self._setc(self.DL1_U2,((50*((self._delay(self.DL1_U1,1e-08)+50*self._delay(self.DL1_I1,1e-08))*187500)+(self._delay(self.DL1_U1,1e-08)+50*self._delay(self.DL1_I1,1e-08))*9375000)+(self._delay(self.DL2_U2,1e-08)+50*self._delay(self.DL2_I2,1e-08))*18750000)/56250000)
		self._setc(self.DL2_U1,((50*((self._delay(self.DL1_U1,1e-08)+50*self._delay(self.DL1_I1,1e-08))*187500)+(self._delay(self.DL1_U1,1e-08)+50*self._delay(self.DL1_I1,1e-08))*9375000)+(self._delay(self.DL2_U2,1e-08)+50*self._delay(self.DL2_I2,1e-08))*18750000)/56250000)
		self._setc(self.R1_U,((50*((self._delay(self.DL1_U1,1e-08)+50*self._delay(self.DL1_I1,1e-08))*187500)+(self._delay(self.DL1_U1,1e-08)+50*self._delay(self.DL1_I1,1e-08))*9375000)+(self._delay(self.DL2_U2,1e-08)+50*self._delay(self.DL2_I2,1e-08))*18750000)/56250000)
		self._setc(self.DL2_A,1)
		self._setc(self.DL2_U2,((self._delay(self.DL2_U1,1e-08)+50*self._delay(self.DL2_I1,1e-08))*6250000+50*((self._delay(self.DL2_U1,1e-08)+50*self._delay(self.DL2_I1,1e-08))*250000))/56250000)
		self._setc(self.R3_U,((self._delay(self.DL2_U1,1e-08)+50*self._delay(self.DL2_I1,1e-08))*6250000+50*((self._delay(self.DL2_U1,1e-08)+50*self._delay(self.DL2_I1,1e-08))*250000))/56250000)
		self._setc(self.VP_U,(56250000*(0.5*(math.tanh((self._time()-1e-08)/1e-09)-math.tanh(((self._time()-1e-08)-8e-08)/1e-09))))/56250000)

