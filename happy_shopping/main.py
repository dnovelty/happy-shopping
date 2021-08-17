from concurrent.futures.thread import ThreadPoolExecutor

from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

executor = ThreadPoolExecutor()
configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner(get_project_settings())
# runner.crawl(SessionSpider)
# runner.crawl(MultiStockSpider)
d = runner.join()
d.addBoth(lambda _: reactor.stop())
# executor.submit(ItemFactoryWorker().start_requests)
reactor.run()  # the script will block here until the crawling is finished


# def run_spider(Spider):
