import requests
from infrastructure.timeutil import timestamp
"""[小米维持会话服务。]
"""

session = requests.session()

class SessionService(object):
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
    response_json = response.json()
    lp_url = response_json.get("lp")
    response = session.get(lp_url)
    pass 

  def __save_cookie(self):
    pass
 
