from lazy import *
"""
temporary test function for lazy_add and lazy_mul

"""

def test_lazy_function():
    assert isinstance(add(1,2), LazyOperation) == True

def test_lazy_add():
    thunk = add(1, 2)
    assert isinstance(thunk, LazyOperation) == True
    assert thunk.eval() == 3

def test_lazy_mul():
    thunk = mul(2, 3)
    assert isinstance(thunk, LazyOperation) == True
    assert thunk.eval() == 6

def test_laze_add_mul():
    thunk = mul(add(1, 2), 4)
    assert isinstance(thunk, LazyOperation) == True
    assert thunk.eval() == 12
