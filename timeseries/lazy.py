class LazyOperation:
    """
    LazyOperation

    TODO:
    1. how to test lazy?
    1. test;
    2. documatation;
    """

    def __init__(self, function, *args, **kwargs):
        self._function = function
        self._args = args
        self._kwargs = kwargs

    def eval(self):
        # Recursively eval() lazy args
        new_args = [a.eval() if isinstance(a, LazyOperation) else a for a in self._args]
        new_kwargs = {k: v.eval() if isinstance(v, LazyOperation) else v for k, v in self._kwargs}
        return self._function(*new_args, **new_kwargs)

def lazy(function):
    def create_thunk(*args, **kwargs):
        return LazyOperation(function, *args, **kwargs)
    return create_thunk

"""
#just for test
@lazy
def add(a, b):
    return a + b

@lazy
def mul(a, b):
    return a * b
"""