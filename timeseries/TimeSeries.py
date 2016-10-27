import reprlib
import collections
import math
import numpy as np

class TimeSeries:
    """
    A class with a list of time points and a list of values.

    todo:
    1. add test cases;
    2. add lazy function;

    Parameters
    ----------
    value :
        a list of values
    time:
        a list of times

    Methods
    -------
    __init__(values, times = None):
        return the length of this sequence
    __getitem__(index):
        return the item wiht key equals to index
    __repr__():
        return the representation of this sequence
    __iter__():
        iterator of the value of timeseries
    itervalues():
        iterator of the timeseries value
    itertimes():
        interator of the timeseries times
    iteritems():
        interator of the timeseries times and value pairs
    interpolate(stime_seq)
        return a timeseries sequence with interpolated value calculated by the input times sequence

    Examples
    --------
    """

    def __init__(self, values, times=None):
        if times:
            self._time = list(times)
        else:
            self._time = list(range(len(values)))
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

    def __str__(self):
        if len(self._timeseries) > 5:
            return 'Length: {} [{}, ..., {}]'.format\
            (len(self._timeseries), self._timeseries[0], \
                self._timeseries[-1])
        else:
            return '[' + ', '.join('{}'.format\
                (item for item in self._timeseries)) + ']'

    def __repr__(self):
        if len(self._timeseries) > 5:
            return 'TimeSeries(Length: {} [{}, ..., {}])'.format\
            (len(self._timeseries), self._timeseries[0], \
                self._timeseries[-1])
        else:
            return 'TimeSeries([' + ', '.join('{}'.format\
                (item for item in self._timeseries)) + '])'

    def __iter__(self):
        for item in self._value:
            yield item

    def itervalues(self):
        for item in self._value:
            yield item

    def itertimes(self):
        for item in self._time:
            yield item

    def iteritems(self):
        for item in zip(self._time, self._value):
            yield item

    def interpolate(self, time_seq):
        value_seq = []
        for i_t in time_seq:
            if i_t < self._time[0]:
                value_seq.append(self._time[0])
                continue
            if i_t > self._time[len(self._time) - 1]:
                value_seq.append(self._time[len(self._time) - 1])
                continue
            for i in range(len(self._time) - 1):
                if i_t >= self._time[i] and i_t <= self._time[i + 1]:
                    v_delta = self._value[i + 1] - self._value[i]
                    t_delta = self._time[i + 1] - self._time[i]
                    slop = v_delta / t_delta
                    new_v = slop * (i_t - self._time[i]) + self._value[i]
                    value_seq.append(new_v)
                    break
        return TimeSeries(value_seq, time_seq)