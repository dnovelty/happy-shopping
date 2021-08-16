from infrastructure.interfaces.responseDispatcher import IResponseDispatcher
from infrastructure import responsedispatcher
from infrastructure.entity.request import RequestEntity
from multiprocessing.queues import Queue
import scrapy

class RequestGate(scrapy.Spider):
    name = 'sending request and getting response spider controller'
    
    responseDispatcher:IResponseDispatcher = None
    start_request = None
    def __init__(self, name=None, **kwargs):
        super().__init__(name=name, **kwargs) 
    
    def start_requests(self):
        return self.start_request
    
    def parse(self, response, **kwargs):
        while True:
            requestEntity = None
            responseEntity = None
            requestEntity = RequestGate.responseDispatcher.dispatch(responseEntity)
            yield requestEntity