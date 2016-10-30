from SimulatedTimeSeries import SimulatedTimeSeries
from itertools import count

def make_data(stop=None):
    for value in count():
        if stop and value > stop:
            break
        yield value

def test_produce():

    #test chunk=1
    data = make_data(10)
    simple_ts = SimulatedTimeSeries(data)
    result = list(simple_ts.produce(1))
    assert result == [[(time, value)] for time, value in enumerate(make_data(10))]

    #test chunk>1
    for data_size, chunk_size in [(50, 5), (50,4), (50, 3), (50, 2)]:
        data = make_data(data_size)
        ts = SimulatedTimeSeries(data)
        result = list(ts.produce(chunk_size))
        expect_result = []
        chunk = []
        for time, value in enumerate(make_data(data_size)):
            if len(chunk) >= chunk_size:
                expect_result.append(chunk)
                chunk = []
            chunk.append((time, value))
        if chunk:
            expect_result.append(chunk)
        assert result == expect_result
