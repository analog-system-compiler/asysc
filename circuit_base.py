
# import math
import numpy as np
# import matplotlib.pyplot as plt

class element:

	def __init__(self):
		self.history_x= [0]
		self.history_y= [0]

	def set(self, pos, val):
		self.history_x.append( pos)
		self.history_y.append( val)

class circuit_base:

	delta_timeval = 1e-9
	timeval = 0.

	def __init__(self):
		self.timeval = 0.
		self.delta_timeval = 1e-9

	def delta_time(self):
		return self.delta_timeval

	def time(self):
		return self.timeval
		
	def delay(self, element_arg, delay_arg ):	
		return np.interp( self.timeval - delay_arg, element_arg.history_x, element_arg.history_y )
	
	def simulate(self, duration, nb):
		self.delta_timeval = duration / nb
		for i in range ( 0, nb ):
			self.step()
			self.timeval += self.delta_timeval
			print('Iteration nb {}'.format(i), end='\r')

