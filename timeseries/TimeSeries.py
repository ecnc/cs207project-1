import reprlib
import collections
import math
import numpy as np
from Lazy import lazy, LazyOperation
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
        Initialize a TimeSeries instance, inherited from SizedContainerTimeSeriesInterface
    __getitem__(index):
        Return the item with key equals to index
    __setitem__(index,value):
        Set the value at the index time by value
    __add__(other):
        Add two timeseries' values at each time point
    __sub__(other):
        Subtract by other's value at each time point
    __mul__(other):
        Multiply by other's value at each time point
    __eq__(other):
        Check if two TimeSeries instance are equal
    __abs__():
        Return the L^2 norm of values
    __bool__():
        Return true if the L^2 norm of values is non-zero
    __neg__():
        Return a new Timeseries instance with the opposite number of value at each time point
    __pos__():
        Return a same Timeseries instance
    interpolate(time_seq)
        return a timeseries sequence with interpolated value calculated by the input times sequence
    __repr__():
        Return the representation of this sequence
    __iter__():
        Iterator of the value of timeseries
    itervalues():
        Iterator of the timeseries value
    itertimes():
        Interator of the timeseries times
    iteritems():
        Interator of the timeseries times and value pairs


    Examples
    --------
    """

    def __init__(self, values, times=None):
        """
        Initialize a TimeSeries instance, inherited from SizedContainerTimeSeriesInterface
        self._time: store the times. The default times are the indexes of the values list.
        self._value: store the values
        self._timeseries: time and value tuple, i.e., zip(_time, _value)
        """
        if times:
            self._time = list(times)
        else:
            self._time = list(range(len(values)))
        self._value = list(values)
        self._timeseries = list(zip(self._time, self._value))
        self._dict = {}

    def __setitem__(self, index, value):
        """
        Set the value at the index time by value

        Raise "LookupError" when the index is out of boundary,
        and raise "TypeError" when the value is of illegal type
        """
        self._value[index] = value
        self._timeseries[index] = (self._time[index], value)

    def __add__(self, other):
        """ 
        Add two timeseries' values at each time point

        other: another TimeSeries instance
        Return a new TimeSeries instance 
        Raise "TypeError" when other is not an instance of TimeSeries class,
        and raise "ValueError" when self and other doesn't have exactly same time list
        """ 
        if not isinstance(other, TimeSeries):
            raise TypeError("NotImplemented Error")
        if len(self) != len(other) or self._time != other._time:
            raise ValueError(str(self)+' and '+str(other)+' must have the same time points')
        return TimeSeries(list(map(lambda x: x[0] + x[1], zip(self._value, other._value))), self._time)

    def __sub__(self, other):
        """ 
        Subtract by other's value at each time point

        other: another TimeSeries instance
        Return a new TimeSeries instance 
        Raise "TypeError" when other is not an instance of TimeSeries class,
        and raise "ValueError" when self and other doesn't have exactly same time list
        """ 
        if not isinstance(other, TimeSeries):
            raise TypeError("NotImplemented Error")
        if len(self) != len(other) or self._time != other._time:
            raise ValueError(str(self) + ' and ' + str(other) + ' must have the same time points')
        return TimeSeries(list(map(lambda x: x[0] - x[1], zip(self._value, other._value))), self._time)

    def __mul__(self, other):
        """ 
        Multiply by other's value at each time point

        other: another TimeSeries instance
        Return a new TimeSeries instance 
        Raise "TypeError" when other is not an instance of TimeSeries class,
        and raise "ValueError" when self and other doesn't have exactly same time list
        """ 
        if not isinstance(other, TimeSeries):
            raise TypeError("NotImplemented Error")
        if len(self) != len(other) or self._time != other._time:
            raise ValueError(str(self) + ' and ' + str(other) + ' must have the same time points')
        return TimeSeries(list(map(lambda x: x[0] * x[1]), zip(self._value, other._value)), self._time)

    def __eq__(self, other):
        """ 
        Check if two TimeSeries instance are equal

        other: another TimeSeries instance
        Return true when they are equal, false otherwise 
        Raise "TypeError" when other is not an instance of TimeSeries class,
        and raise "ValueError" when self and other doesn't have exactly same time list
        """ 
        if not isinstance(other, TimeSeries):
            raise TypeError("NotImplemented Error")
        if len(self) != len(other) or self._time != other._time:
            raise ValueError(str(self) + ' and ' + str(other) + ' must have the same time points')
        return self._value == other._value and self._time == other._time

    def __abs__(self):
        """ 
        Return the L^2 norm of values(the root square of the sum of the squared values)
        """ 
        return math.sqrt(sum(x * x for x in self._value))

    def __bool__(self):
        """ 
        Return true if the L^2 norm of values is non-zero, false if it's zero
        """ 
        return bool(abs(self))

    def __neg__(self):
        """ 
        Return a new Timeseries instance with the opposite number of value at each time point
        """ 
        return TimeSeries([-v for v in self._value], self._time)

    def __pos__(self):
        """ 
        Return a new Timeseries instance with the same value at each time point
        """ 
        return TimeSeries(self._value, self._time)

    def interpolate(self, time_seq):
        """ 
        Interpolate new time points from time_seq, the corresponding value is calculated on the assumption
        that the values follow a piecewise-linear function

        Return the new extended TimeSeries instance
        """         
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
