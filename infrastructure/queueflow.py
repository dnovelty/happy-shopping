from enum import Enum
from infrastructure.content import Passenger
from multiprocessing import Queue

class RouteQueue(Enum):
  StockCheck = ()

  def __init__(self):
    self.queue:Queue = Queue()

  
  def get(self) -> Passenger:
    return self.queue.get()

  
  def put(self,val:Passenger):
    self.queue.put(val)

