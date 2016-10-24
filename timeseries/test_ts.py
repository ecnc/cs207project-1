from ts import TimeSeries
from pytest import raises

# test input with zero length
def test_zerolen():
    with raises(ValueError):
        TimeSeries([])

# test non-int or non-float input
def test_wrongtype():
    with raises(TypeError):
        TimeSeries([1, 2, 'hi'])

# test case with no input
def test_noninput():
    with raises(TypeError):
        TimeSeries()

# test typical input
def test_typical():
    assert TimeSeries([1, 2, 3]) == 'TimeSeries([1, 2, 3])'

# test typical print
def test_typical_print():
    assert print(TimeSeries([1, 2, 3]) == '[1, 2, 3], length = 3'

# test long input
#def test_longinput():
#    assert TimeSeries(range(10)) == 'TimeSeries([0, 1, 2, 3, 4, 5, ...])'

# test long print
#def test_long_print():
#    assert print(TimeSeries(range(10)) == '[0, 1, 2, 3, 4, 5, ...], length = 10'

