import abc
from timeseries.TimeSeriesInterface import TimeSeriesInterface
class StreamTimeSeriesInterface(TimeSeriesInterface):
    '''This is the StreamTimeSeriesInterface.
       StreamTimeSeriesInterface inherits from the TimeSeriesInterface.

       Abstract Methods:
       
         __len__: the length of StreamTimeSeriesInterface.
         produce: produce a chunk sized bunch of new elements into the timeseries whenever it is called.
         online_mean: the mean of the StreamTimeSeriesInterface.
         online_std:  the standard devation of the StreamTimeSeriesInterface.

    '''
    @abc.abstractmethod
    def __len__(self):
        "the length of StreamTimeSeriesInterface."

    @abc.abstractmethod #xinyi added
    def produce(self, chunk=1):
        "produce a chunk sized bunch of new elements into the timeseries whenever it is called"
    #@abc.abstractmethod
    #def __getitem__(self,index):
    #    "get the item from SizedContainerTimeSeriesInterface."

    #@abc.abstractmethod
    #def __setitem__(self,index,val):
    #    "set the item in SizedContainerTimeSeriesInterface."

    #@abc.abstractmethod
    #def online_values(self):
    #    "get values from StreamTimeSeriesInterface."

    #@abc.abstractmethod
    #def online_times(self):
    #    "get times from StreamTimeSeriesInterface."

    #@abc.abstractmethod
    #def online_items(self):
    #    "get time-values tuple pairs from StreamTimeSeriesInterface."

    #@abc.abstractmethod
    #def __contains__(self,val)->bool:
    #    "A test for whether item is in set"
    
    #@abc.abstractmethod
    #def online_interpolate(self,inter_time):
    #    "predict the given time value in StreamTimeSeriesInterface."
    
    @abc.abstractmethod
    def online_mean(self):
        "the mean of the StreamTimeSeriesInterface."                                                 
    @abc.abstractmethod
    def online_std(self): 
        "the standard devation of the StreamTimeSeriesInterface."
