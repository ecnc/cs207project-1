from ts import ArrayTimeSeries

array_ts = ArrayTimeSeries(range(0,10,3))

def test_len():
    assert len(array_ts) == 4

def test_getitem(2):
    assert array_ts[2] == 6

def test_setitem(2,1):
    assert array_ts[2] == 1
