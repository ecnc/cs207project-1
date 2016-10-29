import abc
import reprlib

class TimeSeriesInterface(abc.ABC):
    """
    The abstract interface class for timeseries-related classes
    """


    @abc.abstractmethod
    def __str__(self):
        """
        Format output of class (informal)
        """

    @abc.abstractmethod
    def __repr__(self):
        """
        Format output of class
        """

    @abc.abstractmethod
    def __iter__(self):
        """
        Return an iterator
        """

    @abc.abstractmethod
    def itervalues(self):
        """
        Return iterator of values
        """

class SizedContainerTimeSeriesInterface(TimeSeriesInterface):
    """
    Interface of container-like timeseries
    A SizedContainerTimeSeriesInterface instance should at least have the following variables:
        self._time: store the times
        self._value: store the values
        self._timeseries: time and value tuple, i.e., zip(_time, _value)
    """

    @abc.abstractmethod
    def __setitem__(self, index, value):
        """
        Set the value at the position index by value

        This method should raise "LookupError" when the index is out of boundary,
        and raise "TypeError" when the value is of illegal type
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
        Return a new timeseries that is a interpolation of current timeseries, with time given by time_seq
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
        return class_name + '(' + reprlib.repr([item for item in self._timeseries]) + '), length={}'.format(len(self))


class StreamTimeSeriesInterface(TimeSeriesInterface):
    """
    Interface of stream-like timeseries
    """

    @abc.abstractmethod
    def produce(self, chunk=1):
        pass


