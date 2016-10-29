import abc

class TimeSeriesInterface(abc.ABC):
	"""
	The abstract interface class for timeseries-related classes
	"""

	@abc.abstractmethod
	def __str__(self):
		"""
		Format output of class
		"""

	@abc.abstractmethod
	def __repr__(self):
		"""
		Format output of class
		"""

	@abc.abstractmethod
	def __iter__(self):

	@abc.abstractmethod
	def itervalues(self):
		"""
		Return iterator of values
		"""

class SizedContainerTimeSeriesInterface(TimeSeriesInterface):
	"""
	Interface of container-like timeseries
	"""
    @abc.abstractmethod
	def __getitem__(self, index):
		"""
		Return the value at the position indicated by index

		This method should raise "LookupError" when the index is out of boundary
		"""

	@abc.abstractmethod
	def __setitem__(self, index, value):
		"""
		Set the value at the position index by value

		This method should raise "LookupError" when the index is out of boundary,
		and raise "TypeError" when the value is of illegal type
		"""
	@abc.abstractmethod
	def __len__(self):
		"""
		Return the length of timeseries
		"""

	@abc.abstractmethod
	def __contains__(self, value):
		"""
		Return True if value is in the container
		"""

class StreamTimeSeriesInterface(TimeSeriesInterface):
	"""
	Interface of stream-like timeseries
	"""

	@abc.abstractmethod
	def produce(self, chunk=1):
        pass

