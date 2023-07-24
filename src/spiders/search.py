from scraper import Scraper


class SearchSpider(Scraper):
    def _create_search_url(self, query: str):
        query = query.replace(" ", "+")
        return f"https://avamovie3.info/?s={query}"

    def search(self, query: str):
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
