from abc import abstractmethod
from typing import Generic, Sized, TypeVar
from infrastructure.content import Item, Passenger, RouteQueue, T_Passenger, T_RouteLoader 

class IPassengerConsumer(object):

  @abstractmethod 
  def comsumer(self,passenger:T_Passenger) -> T_RouteLoader:
    pass

class IShoppingBeginner(object):
  @abstractmethod
  def begin()->None:
    pass   

class IConsumerRouteDirecter(object):

  def __init__(self,targetQueue:RouteQueue,passengerConsumer:IPassengerConsumer):
    self.targetQueue:RouteQueue
    self.passengerConsumer:IPassengerConsumer
    
  @abstractmethod 
  def monitorQueue(self) -> None:
    pass

