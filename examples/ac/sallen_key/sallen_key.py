import math
import circuit_base
from circuit_base import circuit_base, element

class circuit( circuit_base ):

	def __init__(self):
		super().__init__()
		self.V_U = element('self.V_U')
		self.R1_U = element('self.R1_U')
		self.R2_U = element('self.R2_U')
		self.C1_I = element('self.C1_I')
		self.C2_U = element('self.C2_U')
		self.R1_I = element('self.R1_I')
		self.A_Iin = element('self.A_Iin')
		self.A_Uin = element('self.A_Uin')
		self.R2_I = element('self.R2_I')
		self.C2_I = element('self.C2_I')
		self.C1_U = element('self.C1_U')
		self.V_I = element('self.V_I')
		self.A_Iout = element('self.A_Iout')
		self.A_Uout = element('self.A_Uout')

	def step(self):
		self.V_U.set_f(1, self.freq)
		self.R1_U.set_f(((100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100)*100*100*3.9e-10*self.s*100-100*100*3.9e-10*self.s*(100*100*3.9e-10*self.s*100+10000))/((100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100)*100*100*100*3.9e-10*self.s), self.freq)
		self.R2_U.set_f((100*100*3.9e-10*self.s*100)/((100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100)*100), self.freq)
		self.C1_I.set_f((100*100*3.9e-10*self.s*8.2e-10*self.s)/(100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100), self.freq)
		self.C2_U.set_f(-(((100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100)*100*100*(3.9e-10*self.s*100-100*3.9e-10*self.s)+100*100*3.9e-10*self.s*(100*(100*3.9e-10*self.s*100-100*3.9e-10*self.s*100)-10000))/((100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100)*100*100*100*3.9e-10*self.s)), self.freq)
		self.R1_I.set_f(((100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100)*100*100*3.9e-10*self.s-100*100*3.9e-10*self.s*(100*100*3.9e-10*self.s+100))/((100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100)*100*100*100*3.9e-10*self.s), self.freq)
		self.A_Iin.set_f(0, self.freq)
		self.A_Uin.set_f(0, self.freq)
		self.R2_I.set_f((100*100*3.9e-10*self.s)/((100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100)*100), self.freq)
		self.C2_I.set_f((100*100*3.9e-10*self.s)/((100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100)*100), self.freq)
		self.C1_U.set_f((100*100*3.9e-10*self.s)/(100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100), self.freq)
		self.V_I.set_f((100*100*3.9e-10*self.s*(100*100*3.9e-10*self.s+100)-(100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100)*100*100*3.9e-10*self.s)/((100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100)*100*100*100*3.9e-10*self.s), self.freq)
		self.A_Iout.set_f((((100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100)*100*100*3.9e-10*self.s-100*100*3.9e-10*self.s*(100*100*3.9e-10*self.s+100))*(100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100)*100-(100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100)*100*100*100*3.9e-10*self.s*100*100*3.9e-10*self.s)/((100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100)*100*100*100*3.9e-10*self.s*(100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100)*100), self.freq)
		self.A_Uout.set_f(-(((100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100)*100*100*(3.9e-10*self.s*100-100*3.9e-10*self.s)+100*100*3.9e-10*self.s*(100*(100*100*3.9e-10*self.s-100*3.9e-10*self.s*100)-10000))/((100*(100*100*3.9e-10*self.s*8.2e-10*self.s+100*3.9e-10*self.s+100*3.9e-10*self.s)+100)*100*100*100*3.9e-10*self.s)), self.freq)

