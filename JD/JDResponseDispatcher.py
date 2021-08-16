from JD.spiders.LoginSpider import LoginSpider
from infrastructure.entity.response import ResponseEntity
from infrastructure.entity.request import RequestEntity
from infrastructure.interfaces.responseDispatcher import IResponseDispatcher


class JDResponseDispatcher(IResponseDispatcher):

    def __init__(self):
        self.loginSpider:LoginSpider = LoginSpider()


    def dispatch(self,responseEntity:ResponseEntity)->RequestEntity:
        
        pass