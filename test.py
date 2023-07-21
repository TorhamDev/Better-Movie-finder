import scrapy
from scrapy.crawler import CrawlerProcess
from src.settings import SETTINGS
from scrapy.selector import Selector


class SearchSpider(scrapy.Spider):
    name = "test"
    url = "https://avamovie2.info/?s=spider+man"
    search_result: list[Selector] = list()

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        result = response.xpath("/html/body/main/div[2]/div/div[2]/article")
        self.search_result.extend(result)
        next_page = (
            response.xpath("/html/body/main/div[2]/div/div[2]/div/a")
            .css(".next")
            .xpath("@href")
            .get()
        )
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


if __name__ == "__main__":
    process = CrawlerProcess(settings=SETTINGS)
    process.crawl(SearchSpider)
    process.start()
