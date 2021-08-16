from JD.entities.LoginEntity import LoginEntity


class LoginSpider(object):
    def start_requests(self):
        pass
    
    def parse(self, response, **kwargs) ->LoginEntity:
        pass