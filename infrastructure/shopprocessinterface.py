from abc import abstractmethod
from typing import Generic, Sized, TypeVar
from infrastructure.content import Item, Passenger, RouteQueue 

class IShopProcessing(object):

  @abstractmethod 
  def process(self,passenger:Passenger) -> Passenger:
    pass


class IShopProcessingBeginner(object):
  
  @abstractmethod 
  def process(self) -> None:
    pass

class IRouteDirecter(object):

  def __init__(self,targetQueue:RouteQueue,shopProcessing:IShopProcessing):
    self.targetQueue:RouteQueue
    self.shopProcessing:IShopProcessing
    
  @abstractmethod 
  def monitorQueue(self) -> None:
    pass