import numpy as np 
class ArrayTimeSeries(TimeSeries):
	def __init__(self):
		if times:
			self._time = np.array(times)
		self._value = np.array(values)