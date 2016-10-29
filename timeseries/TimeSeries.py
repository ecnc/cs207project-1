import reprlib
import collections
import math
import numpy as np
from Lazy import lazy
from Interface import SizedContainerTimeSeriesInterface

class TimeSeries(SizedContainerTimeSeriesInterface):
    """
    A class with a list of time points and a list of values.

    TODO:
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
        self._timeseries = list(zip(self._time, self._value))
        self._dict = {}

    def __setitem__(self, index, value):
        self._value[index] = value
        self._timeseries[index] = (self._time[index], value)

    def __add__(self, other):
        if not isinstance(other, TimeSeries):
            raise TypeError("NotImplemented Error")
        if len(self) != len(other) or self._time != other._time:
            raise ValueError(str(self)+' and '+str(other)+' must have the same time points')
        return TimeSeries(list(map(lambda x: x[0] + x[1], zip(self._value, other._value))), self._time)

    def __sub__(self, other):
        if not isinstance(other, TimeSeries):
            raise TypeError("NotImplemented Error")
        if len(self) != len(other) or self._time != other._time:
            raise ValueError(str(self) + ' and ' + str(other) + ' must have the same time points')
        return TimeSeries(list(map(lambda x: x[0] - x[1], zip(self._value, other._value))), self._time)

    def __mul__(self, other):
        if not isinstance(other, TimeSeries):
            raise TypeError("NotImplemented Error")
        if len(self) != len(other) or self._time != other._time:
            raise ValueError(str(self) + ' and ' + str(other) + ' must have the same time points')
        return TimeSeries(list(map(lambda x: x[0] * x[1]), zip(self._value, other._value)), self._time)

    def __eq__(self, other):
        if not isinstance(other, TimeSeries):
            raise TypeError("NotImplemented Error")
        if len(self) != len(other) or self._time != other._time:
            raise ValueError(str(self) + ' and ' + str(other) + ' must have the same time points')
        return self._value == other._value and self._time == other._time

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self._value))

    def __bool__(self):
        return bool(abs(self))

    def __neg__(self):
        return TimeSeries([-v for v in self._value], self._time)

    def __pos__(self):
        return TimeSeries(self._value, self._time)

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
                if self._time[i] <= i_t <= self._time[i + 1]:
                    v_delta = self._value[i + 1] - self._value[i]
                    t_delta = self._time[i + 1] - self._time[i]
                    slop = v_delta / t_delta
                    new_v = slop * (i_t - self._time[i]) + self._value[i]
                    value_seq.append(new_v)
                    break
        return TimeSeries(value_seq, time_seq)

    @property
    def lazy(self):
        # indentity function
        identity = lambda x: x
        return LazyOperation(identity, self)

# lazy test part
@lazy
def check_length(a, b):
    return len(a) == len(b)
