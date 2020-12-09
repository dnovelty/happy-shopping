from typing import overload
from infrastructure.content import Content, Item
from infrastructure.shopprocessinterface import IShopProcessing


class multiprocessingProxy(IShopProcessing):

    def __init__(self,processingInterface:IShopProcessing):
        self.processingInterface = processingInterface
        
    
    def process(self,item:Item,content:Content) ->Item:
        pass

