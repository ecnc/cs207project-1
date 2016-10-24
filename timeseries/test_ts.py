from ts import TimeSeries
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

def test_typical():
    assert TimeSeries([1, 2, 3]) == str('TimeSeries([1, 2, 3])')

