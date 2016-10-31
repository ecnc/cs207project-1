class LazyOperation:
    """
    This is a class which functions as thunk.

    Methods
    -------
    eval(self):
        Recursively evaluate lazy arguments
    create_thunk(*args, **kwargs):
        create thunk for the @lazy-decorated functions
 
    """

    def __init__(self, function, *args, **kwargs):
        “””
        Constructor
 
        Input: one required argument function and arbitrary positional
        and keyword arguments
        The constructor stores them internally
        “””
        self._function = function
        self._args = args
        self._kwargs = kwargs

    def eval(self):
        “””
        Recursively evaluate lazy arguments
        Return function with the arguments
        “””
        new_args = [a.eval() if isinstance(a, LazyOperation) else a for a in self._args]
        new_kwargs = {k: v.eval() if isinstance(v, LazyOperation) else v for k, v in self._kwargs}
        return self._function(*new_args, **new_kwargs)

def lazy(function):
    def create_thunk(*args, **kwargs):
        “””
        Produce chunk for the @lazy-decorated function
        “””
        return LazyOperation(function, *args, **kwargs)
    return create_thunk

