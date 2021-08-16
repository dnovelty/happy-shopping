import queue
import threading
import time

import scrapy
from twisted.internet import task, reactor, threads, defer

from anontaion import de_yield


class ItemFactoryWorker(scrapy.Spider):
    name = 'ItemFactoryWorker'
    item_producted_quque = queue.Queue()
    start_urls = [
        'https://www.baidu.com',
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.skuids = ['4362724']
        self.request = None

    def start_requests(self):
        print(f"循环次数")
        yield scrapy.Request(url='https://www.baidu.com')
        i = 1
        while i < 2:
            time.sleep(1)
            i = i + 1

    def parse(self, response):
        time.sleep(3)
        print("线程spdier")
        url = 'https://order.jd.com/center/list.action'
        headers = {
            ':authority': 'order.jd.com',
            ':method': 'GET',
            ':path': '/center/list.action',
            ':scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',

            'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }
        return scrapy.Request(url=url,  headers=headers)

    @de_yield
    def loop(self, res):
        print('【订单线程[%s]】11111===================================================================='
              % threading.currentThread().ident)
        time.sleep(6)
        print('【订单线程[%s]】22222===================================================================='
              % threading.currentThread().ident)
        self.request = scrapy.Request(url='https://www.hao123.com/')
        list = [scrapy.Request(url='https://www.hao123.com/')]
        yield self.request

    def get_request(self, results):
        for i in results:
            yield i
