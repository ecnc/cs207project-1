import reprlib
import numbers
import collections
import math
import numpy as np
from Lazy import lazy, LazyOperation
from Interface import SizedContainerTimeSeriesInterface

class TimeSeries(SizedContainerTimeSeriesInterface):
    """
    A time series class that implements SizedContainerTimeSeriesInterface, with times and values stored in
    two seperate lists.

    The times and values should be numbers. It implements basic unary functions 
    abs, bool, neg, pos, and binary functions add, sub, mul, eq, and interpolate function.

    >>> A = TimeSeries([3, 4], [1, 2])
    >>> B = TimeSeries([5, 6],[1, 2])
    >>> A + B
    TimeSeries([(8, 1), (10, 2)]), length=2
    >>> A - B
    TimeSeries([(-2, 1), (-2, 2)]), length=2
    >>> A == B
    False
    >>> -A
    TimeSeries([(-3, 1), (-4, 2)]), length=2
    >>> abs(A)
    5.0
  
    """

    def __init__(self, values, times=None):
        """
        Initialize a TimeSeries instance, inherited from SizedContainerTimeSeriesInterface
        self._time: store the times. The default times are the indexes of the values list.
        self._value: store the values
        self._timeseries: time and value tuple, i.e., zip(_time, _value)
        """
        if not isinstance(values, collections.Sequence):
            raise TypeError("Input values must be Sequence")
        if times is not None:
            if not isinstance(times, collections.Sequence):
                raise TypeError("Input times must be Sequence")
            if len(times) != len(values):
                raise ValueError("Input values sequence and times sequence must have the same length")
            self._time = list(times)
        else:
            self._time = list(range(len(values)))
        self._value = list(values)
        self._timeseries = list(zip(self._value, self._time))

    def __setitem__(self, index, value):
        """
        Set the value at the index time by value

        Raise "LookupError" when the index is out of boundary,
        and raise "TypeError" when the value is of illegal type
        """
        if not isinstance(index, numbers.Integral):
            raise TypeError("Input index must be integer")
        if index >= len(self._value):
            raise ValueError("Input index is out of boundary")
        self._value[index] = value
        self._timeseries[index] = (value, self._time[index])

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
        if len(self) != len(other):
            raise ValueError(str(self)+' and '+str(other)+' must have the same length')
        if self._time != other._time:
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
        if len(self) != len(other):
            raise ValueError(str(self)+' and '+str(other)+' must have the same length')
        if self._time != other._time:
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
        if len(self) != len(other):
            raise ValueError(str(self)+' and '+str(other)+' must have the same length')
        if self._time != other._time:
            raise ValueError(str(self) + ' and ' + str(other) + ' must have the same time points')
        return TimeSeries(list(map(lambda x: x[0] * x[1], zip(self._value, other._value))), self._time)

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
        if len(self) != len(other):
            raise ValueError(str(self) + ' and ' + str(other) + ' must have the same length')
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

        Input must be a Python sequence

        Return a TimeSeries instance with time_seq as times and interpolated values as values
        """
        if not isinstance(time_seq, collections.Sequence):
            raise TypeError("Input must be Sequence")
        value_seq = []
        for i_t in time_seq:
            if i_t < self._time[0]:
                value_seq.append(self._value[0])
                continue
            if i_t > self._time[len(self._time) - 1]:
                value_seq.append(self._value[len(self._value) - 1])
                continue
            for i in range(len(self._time) - 1):
                if self._time[i] <= i_t and i_t <= self._time[i + 1]:
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


