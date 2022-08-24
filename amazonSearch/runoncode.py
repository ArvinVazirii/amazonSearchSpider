from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from amazonSearch.spiders.getCategories import getCategories
from amazonSearch.spiders.search import search

configure_logging()
setting = get_project_settings()
runner = CrawlerRunner(setting)
runner.crawl(getCategories)
runner.crawl(search)
run = runner.join()
run.addBoth(lambda _: reactor.stop())
reactor.run()
