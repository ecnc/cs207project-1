from ts import TimeSeries
from pytest import raises

ts = TimeSeries(range(0,10,3))

def test_iter():
	assert list(ts) == [0,3,6,9]

def test_itertimes():
	assert list(ts.itertimes()) == [0,1,2,3]

def test_iteritems():
	assert list(ts.iteritems()) == [(0,0),(1,3),(2,6),(3,9)]

