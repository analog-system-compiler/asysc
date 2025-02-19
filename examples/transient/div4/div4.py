
# This file was automatically generated by the ASysC compiler. Don't modify it.


import math
import circuit_base
from circuit_base import circuit_base, element

class circuit( circuit_base ):

	def __init__(self):
		super().__init__()
		self.NOT1_VCC = element('NOT1_VCC')
		self.NOT1_Iout = element('NOT1_Iout')
		self.NOT0_Iout = element('NOT0_Iout')
		self.FF1_Iout = element('FF1_Iout')
		self.FF0_Iout = element('FF0_Iout')
		self.V2_I = element('V2_I')
		self.V1_I = element('V1_I')
		self.V2_U = element('V2_U')
		self.FF0_Uclk = element('FF0_Uclk')
		self.FF0_VCC = element('FF0_VCC')
		self.FF0_Uout = element('FF0_Uout')
		self.FF0_aux2 = element('FF0_aux2')
		self.FF0_aux1 = element('FF0_aux1')
		self.NOT0_Uin = element('NOT0_Uin')
		self.NOT0_Uout = element('NOT0_Uout')
		self.FF0_Uin = element('FF0_Uin')
		self.FF1_VCC = element('FF1_VCC')
		self.FF1_Uout = element('FF1_Uout')
		self.FF1_aux2 = element('FF1_aux2')
		self.FF1_aux1 = element('FF1_aux1')
		self.NOT1_Uin = element('NOT1_Uin')
		self.FF1_Uclk = element('FF1_Uclk')
		self.NOT1_Uout = element('NOT1_Uout')
		self.FF1_Uin = element('FF1_Uin')
		self.NOT0_VCC = element('NOT0_VCC')
		self.V1_U = element('V1_U')

	def compute_t(self):
		self._setc(self.NOT1_VCC, 5)
		self._setc(self.NOT1_Iout, 0)
		self._setc(self.NOT0_Iout, 0)
		self._setc(self.FF1_Iout, 0)
		self._setc(self.FF0_Iout, 0)
		self._setc(self.V2_I, 0)
		self._setc(self.V1_I, 0)
		self._setc(self.V2_U, 1.25*(math.tanh(((self._time()+5e-05)%0.0001-5e-05)/1e-09)-math.tanh((self._time()%0.0001-5e-05)/1e-09))+2.5)
		self._setc(self.FF0_Uclk, 1.25*(math.tanh(((self._time()+5e-05)%0.0001-5e-05)/1e-09)-math.tanh((self._time()%0.0001-5e-05)/1e-09))+2.5)
		self._setc(self.FF0_VCC, 5)
		self._setc(self.FF0_Uout, ((self._last(self.FF0_Uin)>self._last(self.FF0_VCC)/2)*(self._last(self.FF0_aux2)==1)+(self._last(self.FF0_Uout)>self._last(self.FF0_VCC)/2)*(self._last(self.FF0_aux2)!=1))*5)
		self._setc(self.FF0_aux2, (self._last(self.FF0_Uclk)>self._last(self.FF0_VCC)/2)&(self._last(self.FF0_aux1)==0))
		self._setc(self.FF0_aux1, self._last(self.FF0_Uclk)>self._last(self.FF0_VCC)/2)
		self._setc(self.NOT0_Uin, ((self._last(self.FF0_Uin)>self._last(self.FF0_VCC)/2)*(self._last(self.FF0_aux2)==1)+(self._last(self.FF0_Uout)>self._last(self.FF0_VCC)/2)*(self._last(self.FF0_aux2)!=1))*5)
		self._setc(self.NOT0_Uout, (self._last(self.NOT0_Uin)<=self._last(self.NOT0_VCC)/2)*5)
		self._setc(self.FF0_Uin, (self._last(self.NOT0_Uin)<=self._last(self.NOT0_VCC)/2)*5)
		self._setc(self.FF1_VCC, 5)
		self._setc(self.FF1_Uout, ((self._last(self.FF1_Uin)>self._last(self.FF1_VCC)/2)*(self._last(self.FF1_aux2)==1)+(self._last(self.FF1_Uout)>self._last(self.FF1_VCC)/2)*(self._last(self.FF1_aux2)!=1))*5)
		self._setc(self.FF1_aux2, (self._last(self.FF1_Uclk)>self._last(self.FF1_VCC)/2)&(self._last(self.FF1_aux1)==0))
		self._setc(self.FF1_aux1, self._last(self.FF1_Uclk)>self._last(self.FF1_VCC)/2)
		self._setc(self.NOT1_Uin, ((self._last(self.FF1_Uin)>self._last(self.FF1_VCC)/2)*(self._last(self.FF1_aux2)==1)+(self._last(self.FF1_Uout)>self._last(self.FF1_VCC)/2)*(self._last(self.FF1_aux2)!=1))*5)
		self._setc(self.FF1_Uclk, ((self._last(self.FF0_Uin)>self._last(self.FF0_VCC)/2)*(self._last(self.FF0_aux2)==1)+(self._last(self.FF0_Uout)>self._last(self.FF0_VCC)/2)*(self._last(self.FF0_aux2)!=1))*5)
		self._setc(self.NOT1_Uout, (self._last(self.NOT1_Uin)<=self._last(self.NOT1_VCC)/2)*5)
		self._setc(self.FF1_Uin, (self._last(self.NOT1_Uin)<=self._last(self.NOT1_VCC)/2)*5)
		self._setc(self.NOT0_VCC, 5)
		self._setc(self.V1_U, 5)

