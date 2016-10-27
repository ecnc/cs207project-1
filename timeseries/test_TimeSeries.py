from TimeSeries import TimeSeries
from ArrayTimeSeries import ArrayTimeSeries
from pytest import raises

"""
test function

todo:
1. add more testcases;

"""


def test_valid_input():
    ts = TimeSeries([1,2],[3,4])
    assert ts._value == [1,2]
    assert ts._time == [3,4]

def test_interpolate():
    a = TimeSeries([1,2,3], [0,5,10])
    b = TimeSeries([100, -100], [2.5,7.5])
    c = a.interpolate([1])
    assert c._value == [1.2]
    assert c._time == [1]
    a.interpolate(b.itertimes()) == TimeSeries([1.5, 2.5], [2.5,7.5])

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