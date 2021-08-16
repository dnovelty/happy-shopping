from enum import Enum
from multiprocessing import set_executable
from typing import List, TypeVar
from multiprocessing import Queue



class Item(object):
    pass

T_Item = TypeVar("T_Item",bound=Item)

class Content(object):
    pass

class Passenger(object):
    def __init__(self,items:List[T_Item],content:Content):
        self.items:List[T_Item]
        self.content:Content

T_Passenger = TypeVar("T_Passenger",bound=Passenger)

class RouteQueue(Enum):
  StockCheck = ()

  def __init__(self):
    self.queue:Queue = Queue()

  
  def get(self) -> T_Passenger:
    return self.queue.get()

  
  def put(self,val:T_Passenger):
    self.queue.put(val)



class RouteLoader(object):
    def __init__(self,route:RouteQueue,passenger:Passenger):
        self.route:RouteQueue
        self.passenger:Passenger

T_RouteLoader = TypeVar("T_RouteLoader",bound=RouteLoader)


