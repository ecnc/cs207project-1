import reprlib
class TimeSeries:
    """
    class TimeSeries:
    A class that takes a list with numerical values.
    Input must be 'int' or 'float' types.
    print(TimeSeries) will return its first 6 elements together with its length.
    """
    def __init__(self, data=None):
	# check input length and typ
        if type(data).__name__ != 'NoneType':
            # check input length
            if  len(data) == 0:
                raise ValueError("input must be with length of at least 1")
            # check input type
            if any(not isinstance(x, int) and not isinstance(x, float) for x in data):
                raise TypeError("can only take 'int' and 'float' types as input")
        else:
            raise TypeError("warning: there is no input!")

        # start to append data
        self._data = []
        if data:
            for item in data:
                self._data.append(item)
                
    def __len__(self):
        return len(self._data)
    
    def __getitem__(self, key):
        return self._data[key]
    
    def __setitem__(self, key, value):
        self._data[key] = value
        return True
    
    def __repr__(self):
        class_name = type(self).__name__
        return "%s(%s)" % (class_name, reprlib.repr(self._data))
    def __str__(self):
        self._len = len(self._data)
        return "%s, length = %s" % (reprlib.repr(self._data), self._len)

    def __iter__(self):
        for item in self._data:
            yield item

    def itertimes(self):
        for i,item in enumerate(self._data):
            yield i

    def iteritems(self):
        for i,item in enumerate(self._data):
              yield (i,item)
    
    
import numpy as np 
class ArrayTimeSeries(TimeSeries):
    """
    Implementation of ArrayTimeSeries
    """
    def __init__(self, data):
        if data:
            self._data = np.array(data)
        else:
            self._data = np.array([])    
            
   
    
    
    

