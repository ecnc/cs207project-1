import numpy as np
from TimeSeries import *
from ArrayTimeSeries import *
from pytest import raises

"""
test function

TODO:
1. add more testcases;
2. test rept and str

"""
def test_valid_input():
    ts = ArrayTimeSeries([3, 4], [1, 2])
    assert np.all(ts._value == [3, 4]) == True
    assert np.all(ts._time == [1, 2]) == True

def test_len():
    ts = ArrayTimeSeries([3, 4], [1, 2])
    assert len(ts) == 2

def test_getitem():
    ts = ArrayTimeSeries([3, 4], [1, 2])
    assert np.all(ts[1] == (4, 2)) == True

def test_setitem():
    ts = ArrayTimeSeries([3, 4], [1, 2])
    ts[0] = 10
    assert np.all(ts[0] == (10, 1)) == True
"""
def test_repr():
    ts = ArrayTimeSeries(list(range(10)), list(range(1, 11)))
    assert repr(ts) == "TimeSeries(Length: 10, [[0 1], [1 2], ..., [9 10]])"

def test_str():
    ts = ArrayTimeSeries(list(range(10)), list(range(1, 11)))
    assert str(ts) == "Length: 10, [[0 1], [1 2], ..., [9 10]]"
"""

def test_contains():
    ts = ArrayTimeSeries(list(range(10)), list(range(1, 11)))
    assert (0 in ts) == True

def test_add():
    ts_1 = ArrayTimeSeries([3, 4], [1, 2])
    ts_2 = ArrayTimeSeries([3, 4], [1, 2])
    ts_sum = ts_1 + ts_2
    assert np.all(ts_sum._value == [6, 8]) == True
    assert ts_sum == ArrayTimeSeries([6, 8], [1, 2])

def test_sub():
    ts_1 = ArrayTimeSeries([3, 4], [1, 2])
    ts_2 = ArrayTimeSeries([3, 4], [1, 2])
    ts_sub = ts_1 - ts_2
    assert ts_sub == ArrayTimeSeries([0, 0], [1, 2])

def test_abs():
    ts = ArrayTimeSeries([3, 4], [3, 4])
    assert abs(ts) == 5

def test_bool():
    ts = ArrayTimeSeries([3, 4], [2, 2])
    assert bool(ts) == True

def test_neg():
    ts = ArrayTimeSeries([3, 4], [2, 2])
    assert np.all(-ts == ArrayTimeSeries([-3, -4], [2, 2])) == True

def test_interpolate():
    ts_1 = ArrayTimeSeries([1, 2, 3], [0, 5, 10])
    ts_2 = ArrayTimeSeries([100, -100], [2.5, 7.5])
    ts_interpolate = ts_1.interpolate([1])
    assert ts_interpolate._value == [1.2]
    assert ts_interpolate._time == [1]


def test_lazy_in_TS_class():
    ts = ArrayTimeSeries([3, 4], [1, 2])
    thunk = ts.lazy
    assert isinstance(thunk, LazyOperation) == True
    assert thunk.eval() == ts

def test_lazy_check_length():
    l1 = ArrayTimeSeries(range(1, 4), range(0, 3))
    l2 = ArrayTimeSeries(range(2, 5), range(1, 4))
    thunk = check_length(l1,l2)
    assert isinstance(thunk, LazyOperation) == True
    assert thunk.eval() == True;


"""
def test_zerolen():
    with raises(ValueError):
        TimeSeries([])

def test_wrongtype():
    with raises(TypeError):
        TimeSeries([1, 2, 'hi'])

def test_noninput():
    with raises(TypeError):
        TimeSeries()

def test_typical_input_repr():
    assert repr(TimeSeries([1, 2, 3])) == 'TimeSeries([1, 2, 3])'

def test_iter():
    ts = TimeSeries(range(0,10,3))
    assert list(ts) == [0,3,6,9]

def test_itertimes():
    ts = TimeSeries(range(0,10,3))
    assert list(ts.itertimes()) == [0,1,2,3]

def test_iteritems():
    ts = TimeSeries(range(0,10,3))
    assert list(ts.iteritems()) == [(0,0),(1,3),(2,6),(3,9)]

def test_typical_input_str():
    assert str(TimeSeries([1, 2, 3])) == '[1, 2, 3], length = 3'

def test_long_input_repr():
    assert repr(TimeSeries(range(10))) == 'TimeSeries([0, 1, 2, 3, 4, 5, ...])'

def test_long_input_str():
    assert str(TimeSeries(range(10))) == '[0, 1, 2, 3, 4, 5, ...], length = 10'

def test_len():
    array_ts = ArrayTimeSeries(range(0,10,3))   
    assert len(array_ts) == 4

def test_getitem():
    array_ts = ArrayTimeSeries(range(0,10,3))
    assert array_ts[2] == 6
"""