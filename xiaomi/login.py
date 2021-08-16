from requests.sessions import session
from infrastructure.timeutil import timestamp
from  xiaomi.session import session

'''
登录服务
'''
class LoginService(object):
  def __init__(self):
    self.loginUrl:str='''https://c3.lp.account.xiaomi.com/longPolling/loginUrl?
    callback=http%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252F%26sign%3DNzY3MDk1YzczNmUwMGM4ODAxOWE0NjRiNTU5ZGQyMzFhYjFmOGU0Nw%2C%2C
    &sid=mi_eshop
    &_bannerBiz=mistore
    &_qrsize=180
    &_locale=zh_CN&_={}'''.format(timestamp())
    pass

  def doLogin(self):
    response = session.get(self.loginUrl) 
    response.json()
    pass 
