import numpy as np 
from TimeSeries import TimeSeries 

class ArrayTimeSeries(TimeSeries):
	"""
	ArrayTimeSeries.

	TODO:
	1. testcases;
	2. documents
	"""
	def __init__(self, times, values):		
		self._time = np.array(times)
		self._value = np.array(values)
