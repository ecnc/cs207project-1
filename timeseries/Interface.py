import abc
import reprlib
import numpy as np

class TimeSeriesInterface(abc.ABC):
    """ Interface class for TimeSeries.
    The is an abstract interface class for timeseries-related classes.
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
        Set the value at the postion index by value
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
        Return a new timeseries that is a interpolation of current timeseries, with time stamps given by time_seq
    mean(self):
        Return mean of self._value
    std(self):
        Return standard deviation of self._value

    
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
        return np.mean(self._value)
        """
        Return mean of self._value
        """

    def std(self):
        return np.std(self._value)
        """
        Return standard deviation of self._value
        """

    def __len__(self):
        return len(self._value)

    def __getitem__(self, index):
        return self._timeseries[index]

    def __iter__(self):
        for item in self._value:
            yield item

    def __contains__(self, val):
        return val in self._value

    def values(self):
        return self._value

    def times(self):
        return self._time

    def items(self):
        return self._timeseries

    def itervalues(self):
        for item in self._value:
            yield item

    def itertimes(self):
        for item in self._time:
            yield item

    def iteritems(self):
        for item in zip(self._time, self._value):
            yield item


    def __str__(self):
        class_name = type(self).__name__
        return class_name + '(' + reprlib.repr([item for item in self._timeseries])

    def __repr__(self):
        class_name = type(self).__name__
        return class_name + '(' + reprlib.repr([item for item in self._timeseries]) + '), \
        length={}'.format(len(self))


class StreamTimeSeriesInterface(TimeSeriesInterface):
    """
    Interface of stream-like timeseries
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
