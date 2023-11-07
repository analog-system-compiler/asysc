import math
import circuit_base
from circuit_base import circuit_base, element

class circuit( circuit_base ):


	def __init__(self):
		super().__init__()

		self.VP_U = element('self.VP_U')
		self.R2_U = element('self.R2_U')
		self.L1_U = element('self.L1_U')
		self.C1_I = element('self.C1_I')
		self.R1_U = element('self.R1_U')
		self.C1_U = element('self.C1_U')
		self.L1_I = element('self.L1_I')
		self.VP_I = element('self.VP_I')
		self.R2_I = element('self.R2_I')
		self.R1_I = element('self.R1_I')

	def step(self):
		self.VP_U.set_t(0.5*(math.tanh((self.time()-2e-08)/1e-09)-math.tanh((self.time()-2e-08-2e-07)/1e-09)))
		self.R2_U.set_t(0)
		self.L1_U.set_t(((1e-09*self._der1(self.C1_U)*(0.5*(math.tanh((self.time()-2e-08)/1e-09)-math.tanh((self.time()-2e-08-2e-07)/1e-09))-7e-09*self._der0(self.L1_I))+1e-09*self._der0(self.C1_U))*7e-09*self._der1(self.L1_I)+(1e-09*self._der1(self.C1_U)+1e-09*self._der1(self.C1_U)*7e-09*self._der1(self.L1_I)+1)*7e-09*self._der0(self.L1_I))/(1e-09*self._der1(self.C1_U)+1e-09*self._der1(self.C1_U)*7e-09*self._der1(self.L1_I)+1))
		self.C1_I.set_t(((1e-09*self._der1(self.C1_U)*(0.5*(math.tanh((self.time()-2e-08)/1e-09)-math.tanh((self.time()-2e-08-2e-07)/1e-09))-7e-09*self._der0(self.L1_I))+1e-09*self._der0(self.C1_U))*1e-09*self._der1(self.C1_U)-(1e-09*self._der1(self.C1_U)+1e-09*self._der1(self.C1_U)*7e-09*self._der1(self.L1_I)+1)*(1e-09*self._der0(self.C1_U)*1e-09*self._der1(self.C1_U)-1e-09*self._der1(self.C1_U)*1e-09*self._der0(self.C1_U)))/((1e-09*self._der1(self.C1_U)+1e-09*self._der1(self.C1_U)*7e-09*self._der1(self.L1_I)+1)*1e-09*self._der1(self.C1_U)))
		self.R1_U.set_t((1e-09*self._der1(self.C1_U)*(0.5*(math.tanh((self.time()-2e-08)/1e-09)-math.tanh((self.time()-2e-08-2e-07)/1e-09))-7e-09*self._der0(self.L1_I))+1e-09*self._der0(self.C1_U))/(1e-09*self._der1(self.C1_U)+1e-09*self._der1(self.C1_U)*7e-09*self._der1(self.L1_I)+1))
		self.C1_U.set_t(((1e-09*self._der1(self.C1_U)*(0.5*(math.tanh((self.time()-2e-08)/1e-09)-math.tanh((self.time()-2e-08-2e-07)/1e-09))-7e-09*self._der0(self.L1_I))+1e-09*self._der0(self.C1_U))-(1e-09*self._der1(self.C1_U)+1e-09*self._der1(self.C1_U)*7e-09*self._der1(self.L1_I)+1)*1e-09*self._der0(self.C1_U))/((1e-09*self._der1(self.C1_U)+1e-09*self._der1(self.C1_U)*7e-09*self._der1(self.L1_I)+1)*1e-09*self._der1(self.C1_U)))
		self.L1_I.set_t((1e-09*self._der1(self.C1_U)*(0.5*(math.tanh((self.time()-2e-08)/1e-09)-math.tanh((self.time()-2e-08-2e-07)/1e-09))-7e-09*self._der0(self.L1_I))+1e-09*self._der0(self.C1_U))/(1e-09*self._der1(self.C1_U)+1e-09*self._der1(self.C1_U)*7e-09*self._der1(self.L1_I)+1))
		self.VP_I.set_t(-((1e-09*self._der1(self.C1_U)*(0.5*(math.tanh((self.time()-2e-08)/1e-09)-math.tanh((self.time()-2e-08-2e-07)/1e-09))-7e-09*self._der0(self.L1_I))+1e-09*self._der0(self.C1_U))/(1e-09*self._der1(self.C1_U)+1e-09*self._der1(self.C1_U)*7e-09*self._der1(self.L1_I)+1)))
		self.R2_I.set_t((1e-09*self._der1(self.C1_U)*(0.5*(math.tanh((self.time()-2e-08)/1e-09)-math.tanh((self.time()-2e-08-2e-07)/1e-09))-7e-09*self._der0(self.L1_I))+1e-09*self._der0(self.C1_U))/(1e-09*self._der1(self.C1_U)+1e-09*self._der1(self.C1_U)*7e-09*self._der1(self.L1_I)+1))
		self.R1_I.set_t((1e-09*self._der1(self.C1_U)*(0.5*(math.tanh((self.time()-2e-08)/1e-09)-math.tanh((self.time()-2e-08-2e-07)/1e-09))-7e-09*self._der0(self.L1_I))+1e-09*self._der0(self.C1_U))/(1e-09*self._der1(self.C1_U)+1e-09*self._der1(self.C1_U)*7e-09*self._der1(self.L1_I)+1))

