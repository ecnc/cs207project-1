import numpy as np
from ArrayTimeSeries import *
from pytest import raises

"""
test function

TODO:
1. add more testcases;
2. test rept and str

"""
def test_valid_full_input():
    ts = ArrayTimeSeries([3, 4], [1, 2])
    assert np.all(ts._value == [3, 4]) == True
    assert np.all(ts._time == [1, 2]) == True

def test_valid_non_times_input():
    ts = ArrayTimeSeries([1, 2])
    assert np.all(ts._value == [1, 2]) == True
    assert np.all(ts._time == [0, 1]) == True

def test_invalid_input():
    with raises(ValueError):
        ArrayTimeSeries([1, 2], [3, 4, 5])
    with raises(TypeError):
        ArrayTimeSeries(1, 2)
    with raises(TypeError):
        ArrayTimeSeries(1, [1])

def test_len():
    ts = ArrayTimeSeries([3, 4], [1, 2])
    assert len(ts) == 2

def test_getitem():
    ts = ArrayTimeSeries([3, 4], [1, 2])
    assert np.all(ts[1] == (4, 2)) == True

def test_valid_input_setitem():
    ts = TimeSeries([1, 2], [3, 4])
    ts[0] = 10
    assert np.all(ts[0] == (3, 10)) == True

def test_invalid_input_setitem():
    ts = TimeSeries([1, 2], [3, 4])
    with raises(ValueError):
        ts[3] = 10
    with raises(TypeError):
        ts[{1}] = 10

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
    assert (11 in ts) == False

def test_valid_input_add():
    ts_1 = ArrayTimeSeries([1, 2], [3, 4])
    ts_2 = ArrayTimeSeries([1, 2], [3, 4])
    ts_sum = ts_1 + ts_2
    assert ts_sum == ArrayTimeSeries([2, 4], [3, 4])

def test_invalid_input_add():
    ts_1 = ArrayTimeSeries([1, 2], [3, 4])
    ts_2 = ArrayTimeSeries([1, 2, 3], [3, 4, 5])
    arry = [1, 2]
    with raises(ValueError):
        ts_sum = ts_1 + ts_2
    with raises(TypeError):
        ts_sum = ts_1 + arry

def test_valid_input_sub():
    ts_1 = ArrayTimeSeries([1, 2], [3, 4])
    ts_2 = ArrayTimeSeries([1, 2], [3, 4])
    ts_sub = ts_1 - ts_2
    assert ts_sub == ArrayTimeSeries([0, 0], [3, 4])

def test_invalid_input_sub():
    ts_1 = ArrayTimeSeries([1, 2], [3, 4])
    ts_2 = ArrayTimeSeries([1, 2, 3], [3, 4, 5])
    arry = [1, 2]
    with raises(ValueError):
        ts_sum = ts_1 - ts_2
    with raises(TypeError):
        ts_sum = ts_1 - arry

def test_valid_input_mul():
    ts_1 = ArrayTimeSeries([1, 2], [3, 4])
    ts_2 = ArrayTimeSeries([1, 2], [3, 4])
    ts_sub = ts_1 * ts_2
    assert ts_sub == ArrayTimeSeries([1, 4], [3, 4])

def test_invalid_input_mul():
    ts_1 = ArrayTimeSeries([1, 2], [3, 4])
    ts_2 = ArrayTimeSeries([1, 2, 3], [3, 4, 5])
    arry = [1, 2]
    with raises(ValueError):
        ts_sum = ts_1 * ts_2
    with raises(TypeError):
        ts_sum = ts_1 * arry

def test_valid_input_eq():
    ts_1 = ArrayTimeSeries([1, 2], [3, 4])
    ts_2 = ArrayTimeSeries([1, 2], [3, 4])
    ts_3 = ArrayTimeSeries([1, 3], [3, 4])
    assert ts_1 == ts_2
    assert ts_1 != ts_3

def test_invalid_input_eq():
    ts_1 = ArrayTimeSeries([1, 2], [3, 4])
    ts_2 = ArrayTimeSeries([1, 2, 3], [3, 4, 5])
    with raises(TypeError):
        ts_1 == ([3, 1], [4, 2])
    with raises(ValueError):
        ts_1 == ts_2

def test_abs():
    ts = ArrayTimeSeries([3, 4], [3, 4])
    assert abs(ts) == 5

def test_bool():
    ts = ArrayTimeSeries([3, 4], [2, 2])
    assert bool(ts) == True

def test_neg():
    ts = ArrayTimeSeries([3, 4], [2, 2])
    assert np.all(-ts == ArrayTimeSeries([-3, -4], [2, 2])) == True

def test_pos():
    ts = ArrayTimeSeries([1, 2], [3, 4])
    assert +ts == ts

def test_valid_input_interpolate():
    ts_1 = ArrayTimeSeries([1,2,3], [0,5,10])
    ts_interpolate_test_1 = ts_1.interpolate([1])
    assert ts_interpolate_test_1._value == [1.2]
    assert ts_interpolate_test_1._time == [1]

    ts_interpolate_test_2 = ts_1.interpolate([-100, 100])
    assert ts_interpolate_test_2 == ArrayTimeSeries([1, 3], [-100, 100])

def test_invalid_input_interpolate():
    ts_1 = ArrayTimeSeries([1, 2, 3], [0, 5, 10])
    ts_2 = ArrayTimeSeries([100, -100], [2.5, 7.5])
    with raises(TypeError):
        ts_1.interpolate(ts_2.itertimes())

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
