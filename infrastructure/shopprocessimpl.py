
from infrastructure.content import T_Passenger
from infrastructure.shopprocessinterface import IRouteDirecter
from infrastructure.executerpool import processingPool


class PerElementNewProcessingRouteDirecterImpl(IRouteDirecter):

    def monitorQueue(self):
        while True:
            passenger = self.targetQueue.get()
            with processingPool as pool:
                pool.apply_async(self.newProcessingToProcess(passenger))

    def newProcessingToProcess(self,passenger:T_Passenger) -> None:
        self.shopProcessing.process(passenger)