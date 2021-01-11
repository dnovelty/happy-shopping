from infrastructure.executerpool import ThreadingPool
from infrastructure.shopprocessimpl import PerElementNewProcessingRouteDirecterImpl
from typing import List
from infrastructure.shopprocessinterface import IConsumerRouteDirecter, IPassengerConsumer, IPassengerProducter, IShoppingBeginner
from infrastructure.queueflow import RouteQueue


class ShoppingBuilder(object):

    def __init__(self):
        self.directors:List[IConsumerRouteDirecter]
        self.shoppingBeginner:IShoppingBeginner
    
    def registerShopProcessing(self,queue:RouteQueue,shopProcessing:IPassengerConsumer) :
        routeDirector = PerElementNewProcessingRouteDirecterImpl(queue,shopProcessing)
        self.directors.append(routeDirector)
        return self

    def setShoppingBeginner(self,shoppingBeginner:IShoppingBeginner):
        self.shoppingBeginner = shoppingBeginner

    def start(self):
        for consumerRouteDirecter in self.directors:
            ThreadingPool.submit(consumerRouteDirecter.monitorQueue)
        self.shoppingBeginner.begin()
