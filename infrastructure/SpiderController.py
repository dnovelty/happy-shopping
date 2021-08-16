from infrastructure.interfaces.responseDispatcher import IResponseDispatcher
from infrastructure import responsedispatcher
from infrastructure.entity.request import RequestEntity
from multiprocessing.queues import Queue
import scrapy
from myqueue import requestQueue

class RequestGate(scrapy.Spider):
    name = 'sending request and getting response spider controller'
    
    needSendingRequestQueue:Queue[RequestEntity] = None
    responseDispatcher:IResponseDispatcher = None
    
    def start_requests(self):
        return super().start_requests()
    
    def parse(self, response, **kwargs):
        while True:
            requestEntity = None
            responseEntity = None
            requestEntity = self.responseDispatcher.dispatch(responseEntity)
            yield requestEntity