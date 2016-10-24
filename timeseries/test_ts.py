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

def test_typical_input_repr():
    assert repr(TimeSeries([1, 2, 3])) == 'TimeSeries([1, 2, 3])'

def test_typical_input_str():
    assert str(TimeSeries([1, 2, 3])) == '[1, 2, 3], length = 3'

def test_long_input_repr():
    assert repr(TimeSeries(range(10))) == 'TimeSeries([0, 1, 2, 3, 4, 5, ...])'

def test_long_input_str():
    assert str(TimeSeries(range(10))) == '[0, 1, 2, 3, 4, 5, ...], length = 10'
