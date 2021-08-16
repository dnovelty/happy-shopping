import os
from JD.entities.LoginEntity import LoginEntity
from infrastructure.mathUtils import int_between 
from infrastructure.timeUtils import millisecond_str
import scrapy
import json


class LoginSpider(object):
    def start_requests(self):
        callback = 'jQuery{}'.format(int_between(1000000, 9999999))
        _ = millisecond_str()
        url = f'https://passport.jd.com/user/petName/getUserInfoForMiniJd.action?callback={callback}&_={_}'

        headers = {
            'Referer': 'https://order.jd.com/center/list.action'
        }
        request = scrapy.Request(url=url, callback=self.login_detect, headers=headers)
        yield request
    
    def parse(self, response, **kwargs) ->LoginEntity:
        pass

    def login_detect(self, response):
        rsp_json = callback_2_json(response.text)
        if not rsp_json:
            return self.do_login(response)
        else:
            return self._session_holder(response)

    def do_login(self, response):
        appid = 133
        size = 147
        t = millisecond_str()
        url = f'https://qr.m.jd.com/show?appid={appid}&size={size}&t={t}'

        headers = {
            'Referer': 'https://passport.jd.com/new/login.aspx'
        }
        return scrapy.Request(url=url, headers=headers, callback=self.open_qr_image)

    def open_qr_image(self, response):
        QRCode_file = 'QRcode.png'
        with open(QRCode_file, 'wb') as f:
            f.write(response.body)
        self._open_image(QRCode_file)
        return self._token_fetch_api(response)

    def _open_image(self, image_file):
        if os.name == "nt":
            os.system('start ' + image_file)  # for Windows
        else:
            if os.uname()[0] == "Linux":
                if "deepin" in os.uname()[2]:
                    os.system("deepin-image-viewer " + image_file)  # for deepin
                else:
                    os.system("eog " + image_file)  # for Linux
            else:
                os.system("open " + image_file)  # for Mac

def callback_2_json(s):
    begin = s.find('{')
    end = s.rfind('}') + 1
    return json.loads(s[begin:end])