from infrastructure.shopprocessimpl import PerElementNewProcessingRouteDirecterImpl
from typing import List
from infrastructure.shopprocessinterface import IRouteDirecter, IShopProcessing, IShopProcessingBeginner
from infrastructure.queueflow import RouteQueue


class ShoppingBuilder(object):

    def __init__(self):
        self.directors:List[IRouteDirecter]
        self.shoppingBeginner:IShopProcessingBeginner
    
    def registerShopProcessing(self,queue:RouteQueue,shopProcessing:IShopProcessing) :
        routeDirector = PerElementNewProcessingRouteDirecterImpl(queue,shopProcessing)
        self.directors.append(routeDirector)
        return self

    def setShoppingBeginner(self,shoppingBeginner:IShopProcessingBeginner):
        self.shoppingBeginner = shoppingBeginner

    def start(self):
        pass
