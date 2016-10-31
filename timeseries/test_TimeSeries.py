from TimeSeries import TimeSeries, check_length, LazyOperation
from pytest import raises

"""
test function

TODO:
1. add more testcases;

"""
def test_valid_full_input():
    ts = TimeSeries([1, 2], [3, 4])
    assert ts._value == [1, 2]
    assert ts._time == [3, 4]

def test_valid_non_times_input():
    ts = TimeSeries([1, 2])
    assert ts._value == [1, 2]
    assert ts._time == [0, 1]

def test_invalid_input():
    with raises(ValueError):
        TimeSeries([1, 2], [3, 4, 5])
    with raises(TypeError):
        TimeSeries(1, 2)
    with raises(TypeError):
        TimeSeries(1, [1])

def test_len():
    ts = TimeSeries([1,2],[3,4])
    assert len(ts) == 2

def test_getitem():
    ts = TimeSeries([1, 2], [3, 4])
    assert ts[1] == (4, 2)

def test_valid_input_setitem():
    ts = TimeSeries([1, 2], [3, 4])
    ts[0] = 10
    assert ts[0] == (3, 10)

def test_invalid_input_setitem():
    ts = TimeSeries([1, 2], [3, 4])
    with raises(ValueError):
        ts[3] = 10
    with raises(TypeError):
        ts[{1}] = 10

def test_contains():
    ts = TimeSeries(list(range(10)), list(range(1, 11)))
    assert (0 in ts) == True

def test_valid_input_add():
    ts_1 = TimeSeries([1, 2], [3, 4])
    ts_2 = TimeSeries([1, 2], [3, 4])
    ts_sum = ts_1 + ts_2
    assert ts_sum == TimeSeries([2, 4], [3, 4])

def test_invalid_input_add():
    ts_1 = TimeSeries([1, 2], [3, 4])
    ts_2 = TimeSeries([1, 2, 3], [3, 4, 5])
    arry = [1, 2]
    with raises(ValueError):
        ts_sum = ts_1 + ts_2
    with raises(TypeError):
        ts_sum = ts_1 + arry

def test_valid_input_sub():
    ts_1 = TimeSeries([1, 2], [3, 4])
    ts_2 = TimeSeries([1, 2], [3, 4])
    ts_sub = ts_1 - ts_2
    assert ts_sub == TimeSeries([0, 0], [3, 4])

def test_invalid_input_sub():
    ts_1 = TimeSeries([1, 2], [3, 4])
    ts_2 = TimeSeries([1, 2, 3], [3, 4, 5])
    arry = [1, 2]
    with raises(ValueError):
        ts_sum = ts_1 - ts_2
    with raises(TypeError):
        ts_sum = ts_1 - arry

def test_valid_input_mul():
    ts_1 = TimeSeries([1, 2], [3, 4])
    ts_2 = TimeSeries([1, 2], [3, 4])
    ts_sub = ts_1 * ts_2
    assert ts_sub == TimeSeries([1, 4], [3, 4])

def test_invalid_input_mul():
    ts_1 = TimeSeries([1, 2], [3, 4])
    ts_2 = TimeSeries([1, 2, 3], [3, 4, 5])
    arry = [1, 2]
    with raises(ValueError):
        ts_sum = ts_1 * ts_2
    with raises(TypeError):
        ts_sum = ts_1 * arry

def test_valid_input_eq():
    ts_1 = TimeSeries([1, 2], [3, 4])
    ts_2 = TimeSeries([1, 2], [3, 4])
    ts_3 = TimeSeries([1, 3], [3, 4])
    assert ts_1 == ts_2
    assert ts_1 != ts_3

def test_invalid_input_eq():
    ts_1 = TimeSeries([1, 2], [3, 4])
    ts_2 = TimeSeries([1, 2, 3], [3, 4, 5])
    with raises(TypeError):
        ts_1 == ([3, 1], [4, 2])
    with raises(ValueError):
        ts_1 == ts_2

def test_abs():
    ts = TimeSeries([3, 4], [3, 4])
    assert abs(ts) == 5

def test_bool():
    ts = TimeSeries([2, 2], [3, 4])
    assert bool(ts) == True

def test_neg():
    ts = TimeSeries([2, 2], [3, 4])
    assert -ts == TimeSeries([-2, -2], [3, 4])

def test_pos():
    ts = TimeSeries([1, 2], [3, 4])
    assert +ts == ts

def test_valid_input_interpolate():
    ts_1 = TimeSeries([1,2,3], [0,5,10])
    ts_interpolate_test_1 = ts_1.interpolate([1])
    assert ts_interpolate_test_1._value == [1.2]
    assert ts_interpolate_test_1._time == [1]

    ts_interpolate_test_2 = ts_1.interpolate([-100, 100])
    assert ts_interpolate_test_2 == TimeSeries([1, 3], [-100, 100])

def test_invalid_input_interpolate():
    ts_1 = TimeSeries([1, 2, 3], [0, 5, 10])
    ts_2 = TimeSeries([100, -100], [2.5, 7.5])
    with raises(TypeError):
        ts_1.interpolate(ts_2.itertimes())

def test_lazy_in_TS_class():
    ts = TimeSeries([1,2],[3,4])
    thunk = ts.lazy
    assert isinstance(thunk, LazyOperation) == True
    assert thunk.eval() == ts

def test_lazy_check_length():
    l1 = TimeSeries(range(0,3), range(1,4))
    l2 = TimeSeries(range(1,4), range(2,5))
    thunk = check_length(l1,l2)
    assert isinstance(thunk, LazyOperation) == True
    assert thunk.eval() == True;
