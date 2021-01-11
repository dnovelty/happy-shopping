
from typing import Iterable, List
from infrastructure.content import Passenger, T_Passenger
from infrastructure.shopprocessinterface import IConsumerRouteDirecter, IProducterRouteDirecter
from infrastructure.executerpool import processingPool


class PerElementNewProcessingRouteDirecterImpl(IConsumerRouteDirecter):

    def monitorQueue(self):
        while True:
            passenger = self.targetQueue.get()
            with processingPool as pool:
                pool.apply_async(self.newProcessingToProcess(passenger))

    

    def newProcessingToProcess(self,passenger:T_Passenger) -> None:
       loader = self.passengerConsumer.comsumer(passenger)
       nextQueue = loader.route
       passenger = loader.passenger
       nextQueue.put(passenger)



 