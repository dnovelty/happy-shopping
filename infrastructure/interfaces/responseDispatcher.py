from infrastructure.entity.request import RequestEntity
from infrastructure.entity.response import ResponseEntity


class IResponseDispatcher(object):
    
    def dispatch(self,responseEntity:ResponseEntity)->RequestEntity:
        pass