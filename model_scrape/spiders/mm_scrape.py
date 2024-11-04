from typing import Iterable
import scrapy


class MmScrapeSpider(scrapy.Spider):
    name = "mm_scrape"

    URLS = "https://www.modelmanagement.com/backend/api/models/search"

    def start_requests(self):
        yield self.parse

    def parse(self, response):
        pass
