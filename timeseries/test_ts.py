from ts import TimeSeries
from ts import ArrayTimeSeries
from pytest import raises
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


