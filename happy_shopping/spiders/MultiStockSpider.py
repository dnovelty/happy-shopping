import math
import queue

import scrapy
from twisted.internet import threads

import config
from anontaion import de_yield
from exception import BizException
from mathUtils import int_between
from timeUtils import millisecond_str


class MultiStockSpider(scrapy.Spider):
    name = 'MultiStockSpider'
    up_stream_queue = None
    multi_processed_queue = queue.Queue()
    start_urls = [
        'https://www.baidu.com',
    ]

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        if not MultiStockSpider.up_stream_queue:
            raise BizException("需指定上游队列")
        if not MultiStockSpider.multi_processed_queue:
            raise BizException("需指定下游队列")
        # 将需要发起多库查询的skuid列表进行分段的大小
        self.segmentation_size = 100

    def start_requests(self):
        thread = threads.deferToThread(self.do_start_requests)
        return thread

    def do_start_requests(self):
        skuIds = MultiStockSpider.up_stream_queue.get()
        for skuids_segment in self.do_skuids_segment(skuIds):
            callback = 'jQuery{}'.format(int_between(1000000, 9999999))
            type = 'getstocks'
            skuIds = ','.join(skuids_segment)
            area = config.area
            _ = millisecond_str()
            url = f'https://c0.3.cn/stocks?callback={callback}&type={type}&skuIds={skuIds}&area={area}&_={_}'
            yield scrapy.Request(url=url)

    def do_skuids_segment(self, skuids):
        skuid_nums = len(skuids)
        skuid_batchs = math.ceil(skuid_nums / self.segmentation_size)
        if skuid_batchs > 1:
            for i in range(0, skuid_batchs):
                if self.segmentation_size * (i + 1) <= skuid_nums:
                    yield skuids[self.segmentation_size * i:self.segmentation_size * (i + 1)]
                else:
                    # skuids最后一段
                    yield self.skuids[self.segmentation_size * i:skuid_nums]
        else:
            yield skuids

    def parse(self, response):
        thread = threads.deferToThread(self.do_parse, response)
        return thread



