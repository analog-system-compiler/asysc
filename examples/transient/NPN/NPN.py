
# Copyright (C) 2006-2024 The Analog System Compiler project

# This file was automatically generated by the ASysC compiler. Don't modify it.


import math
import circuit_base
from circuit_base import circuit_base, element

class circuit( circuit_base ):

	def __init__(self):
		super().__init__()
		self.P1_U = element('P1_U')
		self.Q1_IBC = element('Q1_IBC')
		self.R3_I = element('R3_I')
		self.Q1_IBE = element('Q1_IBE')
		self.R1_I = element('R1_I')
		self.R2_I = element('R2_I')
		self.V2_I = element('V2_I')
		self.V1_I = element('V1_I')
		self.V2_U = element('V2_U')
		self.P2_U = element('P2_U')
		self.R3_U = element('R3_U')
		self.R1_U = element('R1_U')
		self.Q1_UBC = element('Q1_UBC')
		self.R2_U = element('R2_U')
		self.Q1_UBE = element('Q1_UBE')
		self.V1_U = element('V1_U')

	def step(self):
		self._setc(self.P1_U,(((((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*10000)/0.026-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*10000+((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000000))/0.000676-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000))-(1+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000)+((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026-(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000)*(5*(self._time()%1)))/(((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*(10000+((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000000)/0.026))/0.026-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000+10000)+(((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026-1)-(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*11000))
		self._setc(self.Q1_IBC,(((10000*(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))-((10000*(1e-15*math.exp(self._last(self.Q1_UBC)/0.026)))/0.026-1))*(1e-15*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-(1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)+0.01*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-1)))-((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026)+(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000)-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000))/0.000676)*5-(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026)-(1e-15*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)*(5*(self._time()%1))))-((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000-((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026)*(1e-15*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-(1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)+0.01*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-1))))/(((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000-(((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000000))/0.000676-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000))+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000-((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026)+10000*(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))-((10000*(1e-15*math.exp(self._last(self.Q1_UBC)/0.026)))/0.026-1)))
		self._setc(self.R3_I,(((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000-((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026)*(1e-15*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-(1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)+0.01*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-1)))-((10000*(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))-((10000*(1e-15*math.exp(self._last(self.Q1_UBC)/0.026)))/0.026-1))*(1e-15*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-(1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)+0.01*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-1)))-((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026)+(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000)-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000))/0.000676)*5-(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026)-(1e-15*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)*(5*(self._time()%1)))))/(((1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*10000-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*10000)/0.026+(1-((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000))-((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))/0.026-1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026)+10000*(((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*(1e-15*math.exp(self._last(self.Q1_UBE)/0.026)))/0.000676-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026)))-(1e-15*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)*1000))
		self._setc(self.Q1_IBE,(((((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026-1)-(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*11000)*(1e-15*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-(1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)+0.01*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-1)))-((1000*((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))/0.026-1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)+1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))+(10000*(1e-15*math.exp(self._last(self.Q1_UBC)/0.026)))/0.026-10000*(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)))*(1e-15*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-(1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)+0.01*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-1)))-(((((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000))/0.000676-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000))-(1e-15*math.exp(self._last(self.Q1_UBC)/0.026))/0.026)*5-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)-(1e-15*math.exp(self._last(self.Q1_UBC)/0.026))/0.026+(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000)-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*1000))/0.000676)*(5*(self._time()%1)))))/(((((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026-1)-(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*11000)-((1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*10000-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*10000)/0.026+(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000)-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000000))/0.000676)))
		self._setc(self.R1_I,(((((1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)-(1e-15*math.exp(self._last(self.Q1_UBC)/0.026))/0.026+(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000)-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*1000))/0.000676)+1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026)-(1e-15*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)*(5*(self._time()%1))+((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))/0.026-1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*5)+(1000*(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)-(1e-15*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))+1)*(1e-15*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-(1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)+0.01*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-1))))+(1+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000)*(1e-15*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-(1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)+0.01*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-1))))/((1+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000)-((((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*1000))/0.000676-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000))-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)-(1e-15*math.exp(self._last(self.Q1_UBC)/0.026))/0.026+1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026)-(1e-15*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*10000))
		self._setc(self.R2_I,(((((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026-1)-(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*11000)*(1e-15*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-(1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)+0.01*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-1)))-((1000*((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))/0.026-1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)+1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))+(10000*(1e-15*math.exp(self._last(self.Q1_UBC)/0.026)))/0.026-10000*(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)))*(1e-15*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-(1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)+0.01*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-1)))-(((((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000))/0.000676-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000))-(1e-15*math.exp(self._last(self.Q1_UBC)/0.026))/0.026)*5-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)-(1e-15*math.exp(self._last(self.Q1_UBC)/0.026))/0.026+(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000)-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*1000))/0.000676)*(5*(self._time()%1)))))/((((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*10000)/0.026-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*10000+((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000000))/0.000676-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000))-(1+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000)+((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026-(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000))
		self._setc(self.V2_I,(((((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))/0.026-1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*(5*(self._time()%1))+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026)+(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000)-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000))/0.000676)*5)-(1-(10000*(1e-15*math.exp(self._last(self.Q1_UBC)/0.026)))/0.026+10000*(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)))*(1e-15*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-(1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)+0.01*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-1))))-(((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026-(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000)*(1e-15*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-(1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)+0.01*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-1))))/((((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*10000)/0.026-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*10000+((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000000))/0.000676-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000))-(1+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000)+((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026-(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000))
		self._setc(self.V1_I,((1+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000)*(1e-15*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-(1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)+0.01*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-1)))-(((((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))/0.026-1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)-(1e-15*math.exp(self._last(self.Q1_UBC)/0.026))/0.026+(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000)-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*1000))/0.000676))*(5*(self._time()%1))+((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026)+(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000)-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000))/0.000676)+(((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000))/0.000676-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000))-(1e-15*math.exp(self._last(self.Q1_UBC)/0.026))/0.026)*5)-(1000*(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)-(1e-15*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))+((1+10000*((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))/0.026-(1e-15*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))+10000*(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)-1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))))*(1e-15*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-(1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)+0.01*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-1)))))/((((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*10000)/0.026-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*10000+((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000000))/0.000676-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000))-(1+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000)+((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026-(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000))
		self._setc(self.V2_U,(((((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*10000)/0.026-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*10000+((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000000))/0.000676-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000))-(1+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000)+((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026-(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000)*5)/((((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*10000)/0.026-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*10000+((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000000))/0.000676-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000))-(1+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000)+((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026-(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000))
		self._setc(self.P2_U,(((((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000-((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*1000)/0.026)*(5*(self._time()%1))+((1+(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*10000-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*10000)/0.026)+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000-((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026)*5)-(1000*(((10000*(1e-15*math.exp(self._last(self.Q1_UBC)/0.026)))/0.026-1)-10000*(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))))*(1e-15*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-(1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)+0.01*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-1))))-((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000-((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000000)/0.026)*(1e-15*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-(1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)+0.01*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-1))))/(((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000-((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*1000)/0.026)-((((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*10000)/0.026-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*10000)-1+((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026-(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000)+((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*1000)/0.026-10000*(((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*1000))/0.000676-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000))))
		self._setc(self.R3_U,((((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000-(((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000000))/0.000676-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000)))*5-((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000-((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*1000)/0.026)*(5*(self._time()%1))+(1000*(((10000*(1e-15*math.exp(self._last(self.Q1_UBC)/0.026)))/0.026-1)-10000*(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))))*(1e-15*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-(1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)+0.01*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-1))))+((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000-((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000000)/0.026)*(1e-15*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-(1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)+0.01*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-1))))/(((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000+(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000)-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000000))/0.000676)+(1-10000*((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))/0.026-1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026)))-10000*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))/0.026-1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))))
		self._setc(self.R1_U,-(((10000-1000*((10000*(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))-(10000*(1e-15*math.exp(self._last(self.Q1_UBC)/0.026)))/0.026)-10000*(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))))*(1e-15*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-(1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)+0.01*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-1)))-(((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*10000)/0.026)*5-(((1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*10000-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*10000)/0.026+(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000)-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000000))/0.000676)+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000-((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026)*(5*(self._time()%1)))+(10000+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000)*(1e-15*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-(1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)+0.01*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-1))))/(10000*((((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*1000))/0.000676-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000))-(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)-(1e-15*math.exp(self._last(self.Q1_UBC)/0.026))/0.026+1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026)-(1e-15*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))-((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000+1))))
		self._setc(self.Q1_UBC,-(((10000+1000*(1+10000*(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))))*(1e-15*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-(1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)+0.01*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-1)))-((1+((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*1000)/0.026)*(5*(self._time()%1))+(((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026-(1+(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*10000))*5)+(10000+((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000000)/0.026)*(1e-15*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-(1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)+0.01*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-1))))/(((10000+1000*(1+10000*(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))))*(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))-((10000*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))/0.026-1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))+((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*1000)/0.026)-(((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*1000)/0.026+1)))-((10000+((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000000)/0.026)*(1e-15*math.exp(self._last(self.Q1_UBC)/0.026)))/0.026)))
		self._setc(self.R2_U,0)
		self._setc(self.Q1_UBE,-(((10000-1000*((1-(10000*(1e-15*math.exp(self._last(self.Q1_UBC)/0.026)))/0.026)-1))*(1e-15*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-(1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)+0.01*((1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)-1)))-((1+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000)*(5*(self._time()%1))+((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*10000)/0.026)*5)+((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000+10000)*(1e-15*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-(1-self._last(self.Q1_UBC)/0.026)*math.exp(self._last(self.Q1_UBC)/0.026)+0.01*((1-self._last(self.Q1_UBE)/0.026)*math.exp(self._last(self.Q1_UBE)/0.026)-1))))/((1-10000*((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))/0.026-1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000)-((10000-1000*((1-(10000*(1e-15*math.exp(self._last(self.Q1_UBC)/0.026)))/0.026)-1))*(1e-15*math.exp(self._last(self.Q1_UBE)/0.026)))/0.026+((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000+10000)*(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026)))))
		self._setc(self.V1_U,((((1+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000)+((1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*10000-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*10000)/0.026+(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000)-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000000))/0.000676))+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000-((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026)*(5*(self._time()%1)))/(((1+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*1000)+((1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*10000-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*10000)/0.026+(1e-15*(math.exp(self._last(self.Q1_UBE)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBE)/0.026))/0.026))*((1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000000)-((1e-15*math.exp(self._last(self.Q1_UBC)/0.026))*((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000000))/0.000676))+(1e-15*(math.exp(self._last(self.Q1_UBC)/0.026)/0.026+(0.01*math.exp(self._last(self.Q1_UBC)/0.026))/0.026))*10000-((1e-15*math.exp(self._last(self.Q1_UBE)/0.026))*10000)/0.026))

