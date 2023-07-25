from scraper import Scraper  # type: ignore
from scrapy.selector import Selector, SelectorList  # type: ignore
from settings import AVAMOVIE_BASE_URL  # type: ignore


class SearchSpider(Scraper):
    def _create_search_url(self, query: str):
        query = query.replace(" ", "+")
        return f"{AVAMOVIE_BASE_URL}/?s={query}"

    def search(self, query: str) -> SelectorList[Selector]:
        results = list()
        self.url = self._create_search_url(query)
        self.scrap()

        results.extend(self.xpath("/html/body/main/div[2]/div/div[2]/article"))
        while True:
            next_page = (
                self.xpath("/html/body/main/div[2]/div/div[2]/div/a")
                .css(".next")
                .xpath("@href")
                .get()
            )
            if next_page == None:
                break

            self.url = next_page
            self.scrap()
            results.extend(self.xpath("/html/body/main/div[2]/div/div[2]/article"))

        return results
