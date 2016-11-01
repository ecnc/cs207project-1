""" Interface module for TimeSeries.
This module defines abstract interface classes for TimeSeries.

Classes
-------
TimeSeriesInterface(abc.ABC):
    Define a class for all timeseries-related classes
SizedContainerTimeSeriesInterface(TimeSeriesInterface):
    Define a class for container-like timeseries
StreamTimeSeriesInterface(TimeSeriesInterface):
    Define a class for stream-like timeseries

"""

import abc
import reprlib
import numpy as np


class TimeSeriesInterface(abc.ABC):
    """ Interface class for TimeSeries.
    The is an abstract interface class for all timeseries-related classes.
    Common methods that will be used in timeseries-related classes are defined.
    
    Methods
    -------
    __str__(self):
        Format (informal) string output of class
    __repr__(self):
        Format (official) string output of class
    __iter__(self):
        Iterate over values
    itervalues(self):
        Return an iterator of values
    
    """


    @abc.abstractmethod
    def __str__(self):
        """
        Format (informal) string output of class
        """

    @abc.abstractmethod
    def __repr__(self):
        """
        Format (official) string output of class
        """

    @abc.abstractmethod
    def __iter__(self):
        """
        Iterate over values
        """

    @abc.abstractmethod
    def itervalues(self):
        """
        Return an iterator of values
        """

class SizedContainerTimeSeriesInterface(TimeSeriesInterface):
    """ Interface class for SizedContainerTimeSeries.
    This is an abstract interface class for container-like timeseries.
    
    Attributes
    ----------
    A SizedContainerTimeSeriesInterface instance should at least have the following variables.
    self._time:
        store the times
    self._value:
        store the values
    self._timeseries:
        time and value tuple, i.e., zip(_time, _value)
    
    Methods
    -------
    __setitem__(self, index, value):
        Set the value at the postion index
    __add__(self, other):
        Return self + other
    __sub__(self, other):
        Return self - other
    __mul__(self, other):
        Return self * other (element-wise)
    __eq__(self, other):
        Return self == other
    __abs__(self):
        Return abs(self)
    __bool__(self):
        Return bool(self)
    __neg__(self):
        Return neg(self)
    __pos__(self):
        Return pos(self)
    interpolate(self, time_seq):
        Return a new timeseries that is a interpolation of current timeseries, 
        with time stamps given by time_seq
    mean(self):
        Return mean of self._value
    std(self):
        Return standard deviation of self._value
    __len__(self):
        Return length of self._value
    __getitem__(self, index):
        Return the value of self._timeseries at the position index
    __iter__(self):
        Iterate over self._value
    __contains__(self, val):
        Return True if val is in self._value, False otherwise
    values(self):
        Return self._value
    times(self):
        Return self._time
    items(self):
        Return self._timeseries
    itervalues(self):
        Iterate over self._value
    itertimes(self):
        Iterate over self._time
    __str__(self):
        Format (informal) string output of class
    __repr__(self):
        Format (official) string output of class
    
    """

    @abc.abstractmethod
    def __setitem__(self, index, value):
        """
        Set the value at the position index by value

        This method should raise "LookupError" when the index is out of boundary,
        and should raise "TypeError" when the value is of illegal type.
        """

    @abc.abstractmethod
    def __add__(self, other):
        """
        Return self + other
        """

    @abc.abstractmethod
    def __sub__(self, other):
        """
        Return self - other
        """

    @abc.abstractmethod
    def __mul__(self, other):
        """
        Return self * other (element-wise)
        """

    @abc.abstractmethod
    def __eq__(self, other):
        """
        Return self == other
        """

    @abc.abstractmethod
    def __abs__(self):
        """
        Return abs(self)
        """

    @abc.abstractmethod
    def __bool__(self):
        """
        Return bool(self)
        """

    @abc.abstractmethod
    def __neg__(self):
        """
        Return neg(self)
        """

    @abc.abstractmethod
    def __pos__(self):
        """
        Return pos(self)
        """

    @abc.abstractmethod
    def interpolate(self, time_seq):
        """
        Return a new timeseries that is a interpolation of current timeseries, \
        with time stamps given by time_seq
        """

    def mean(self):
        """
        Return mean of self._value
        """
        return np.mean(self._value)


    def std(self):
        """
        Return standard deviation of self._value
        """
        return np.std(self._value)


    def __len__(self):
        """
        Return length of self._value
        """
        return len(self._value)


    def __getitem__(self, index):
        """
        Return the value of self._timeseries at the position index
        """
        return self._timeseries[index]


    def __iter__(self):
        """
        Iterate over self._value
        """
        for item in self._value:
            yield item


    def __contains__(self, val):
        """
        Return True if val is in self._value, False otherwise
        """
        return val in self._value


    def values(self):
        """
        Return self._value
        """
        return self._value


    def times(self):
        """
        Return self._time
        """
        return self._time


    def items(self):
        """
        Return self._timeseries
        """
        return self._timeseries


    def itervalues(self):
        """
        Iterate over self._value
        """
        for item in self._value:
            yield item


    def itertimes(self):
        """
        Iterate over self._time
        """
        for item in self._time:
            yield item

 
    def iteritems(self):
        """
        Iterate over time and value tuple, i.e., zip(_time, _value)
        """
        for item in zip(self._time, self._value):
            yield item


    def __str__(self):
        """
        Format (informal) string output of class
        """
        class_name = type(self).__name__
        return class_name + '(' + reprlib.repr([item for item in self._timeseries])


    def __repr__(self):
        """
        Format (official) string output of class
        """
        class_name = type(self).__name__
        return class_name + '(' + reprlib.repr([item for item in self._timeseries]) +\
               '), length={}'.format(len(self))

class StreamTimeSeriesInterface(TimeSeriesInterface):
    """ Interface class for StreamTimeSeries.
    This is an abstract interface class for stream-like timeseries.
    
    Methods
    -------
    produce(self, chunk=1):
        Produce a chunk sized bunch of new elements into the timeseries whenever it is called
    online_mean(self):
        Return a time series of means
    online_std(self):
        Return a time series of standard deviations
    
    """

    @abc.abstractmethod
    def produce(self, chunk=1):
        """
        Produce a chunk sized bunch of new elements into the timeseries whenever it is called
        """
        pass

    @abc.abstractmethod
    def online_mean(self):
        """
        Return a time series of means
        """

    @abc.abstractmethod
    def online_std(self):
        """
        Return a time series of standard deviations
        """

    @abc.abstractmethod
    def mean(self):
        """
        Return the mean of the complete sequence
        """

    @abc.abstractmethod
    def std(self):
        """
        Return the std of the complete sequence
        """



