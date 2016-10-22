import reprlib
import collections

class TimeSeries:
	def __init__(self, values, times = None):
		if times:
			self_time = list(times)
		self._value = list(values)
		self._timeseries = zip(self._time, self._value)
		self._dict = {}

	def __len__(self):
		return len(self._value)

	def __getitem__(self, index):
		return self._timeseries[index]

	def __setitem__(self, index, value):
		self._value[index] = value
		self._timeseries[index] = (value, index)

	def __repr__(self):
		if len(self._timeseries) > 5:
			return 'TimeSeries(Length: {} [{}, ..., {}])'.format(len(self._timeseries), self._timeseries[0], self._timeseries[-1])
		else:
			return 'TimeSeries([' + ', '.join('{}'.format(item for item in self._timeseries)) + ']'

	def __iter__(slef):
		for item in self._value:
			yield item

	def itertimes(self):
		for item in self._value:
			yeild item

	def itertimes(self):
		for item in self._timeseries:
			yield item

	def interpolate(self, time_seq):
		value_seq = []
		for t in time_seq:
			if t < self._time[0]:
				value_seq.append(self._time[0])
				continue
			if t > self._time[len(self._time) - 1]
				value_seq.append(self._time[len(self._time) - 1])
				continue
			for i in range(len(slef._time) - 1):
				if t > self._time[i] and t < self._time[i+1]:
					v_delta = self._value[i+1] - self._value[i]
					t_delta = self._time[i+1] - self._time[i]
					slop = v_delta / t_delta
					v = slop * (t - self._time[i]) + self._value[i]
					break
			value_seq.append(v)
        return TimeSeries(time_seq, value_seq)
