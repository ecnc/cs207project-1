import reprlib
class TimeSeries:
    """
    Implementation of TimeSeries.
    TODO:
    1. Detailed documentation, including docstrings.
    2. Add tests.
    """
    def __init__(self, data=None):
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

    def __iter__(self):
        for item in self._data:
            yield item

    def itertimes(self):
        for i,item in enumerate(self._data):
            yield i

    def iteritems(self):
        for i,item in enumerate(self._data):
              yield (i,item)
    	
