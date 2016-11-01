from SimulatedTimeSeries import SimulatedTimeSeries
from itertools import count
from random import normalvariate, random
import numpy as np

def make_simple_data(stop=None):
    for value in count():
        if stop and value > stop:
            break
        yield value

def make_stat_data(m, stop=None):
    for _ in count():
        if stop and _ > stop:
            break
        yield 1.0e09 + normalvariate(0, m*random())

def test_produce():
    #test chunk=1 and chunk>1
    for data_size, chunk_size in [(50, 5), (50, 4), (50, 3), (50, 2), (50, 1)]:
        data = make_simple_data(data_size)
        ts = SimulatedTimeSeries(data)
        result = list(ts.produce(chunk_size))
        expect_result = []
        for time, value in enumerate(make_simple_data(data_size)):           
            if len(expect_result) >= chunk_size:
                assert result == expect_result
                result = list(ts.produce(chunk_size))
                expect_result = []
            expect_result.append((time, value))



"""
TODO:
Finish the test function for online_mean and online_std when they are ready

def test_mean_std():
    #test chunk=1 and chunk>1
    for data_size, chunk_size in [(50, 5), (50,4), (50, 3), (50, 2), (50, 1)]:
        np.random.seed(0)
        data = make_simple_data(data_size)
        # data = make_stat_data(5, data_size)
        ts_mean = SimulatedTimeSeries(data).online_mean()
        ts_std = SimulatedTimeSeries(data).online_std()
        result_mean = list(ts_mean.produce(chunk_size))
        result_std = list(ts_std.produce(chunk_size))

        np.random.seed(0)
        data = list(make_stat_data(5, data_size))
        expect_result_mean, expect_result_std = [], []
        chunk_mean, chunk_std = [], []
        for time in range(len(data)):
            if len(chunk_mean) >= chunk_size:
                expect_result_mean.append(chunk_mean)
                expect_result_std.append(chunk_std)
                chunk_mean, chunk_std = [], []
            chunk_mean.append((time, np.mean(data[:time+1])))
            chunk_std.append((time, np.std(data[:time + 1])))

        if chunk_mean:
            expect_result_mean.append(chunk_mean)
            expect_result_std.append(chunk_std)
        assert result_mean == expect_result_mean
        assert result_std == expect_result_std
"""