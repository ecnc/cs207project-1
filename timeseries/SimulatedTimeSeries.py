from Interface import StreamTimeSeriesInterface

class SimulatedTimeSeries(StreamTimeSeriesInterface):
    """
    Stream-like timeseries without storage
    """
    def __init__(self, gen):
        self._gen = gen
        self._time = 0

    def __str__(self):
        class_name = type(self).__name__
        return "{}(time={})".format(class_name, self._time)

    def __repr__(self):
        class_name = type(self).__name__
        return "{}(time={})".format(class_name, self._time)

    def __iter__(self):
        yield from self._gen

    def itervalues(self):
        yield from self._gen

    def produce(self, chunk=1):
        values = []
        while True:
            while len(values) < chunk:
                try:
                    values.append((self._time, next(self._gen)))
                except StopIteration:
                    if values: yield values
                    return
                self._time += 1
            yield values
            values = []

    def online_mean(self):
        """
        Return a SimulatedTimeSeries of means
        """

        def mean_generator():
            n = 0
            mu = 0
            for value in self._iterator:
                n += 1
                delta = value - mu
                mu = mu + delta / n
                yield mu

        return SimulatedTimeSeries(mean_generator)

    def online_std(self):
        """
        Return a SimulatedTimeSeries of standard deviations
        """

        def std_generator():
            n = 0
            mu = 0
            stddev = 0
            dev_accum = 0
            for value in self._iterator:
                n += 1
                delta = value - mu
                old_mu, mu = mu, mu + delta / n
                dev_accum = dev_accum + (value - old_mu) * (value - mu)
                if n > 1:
                    stddev = math.sqrt(dev_accum / (n - 1))
                yield stddev

        return SimulatedTimeSeries(std_generator)
