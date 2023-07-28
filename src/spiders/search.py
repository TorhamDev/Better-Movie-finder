from scraper import Scraper  # type: ignore
from settings import AVAMOVIE_BASE_URL  # type: ignore


class SearchSpider(Scraper):
    def _create_search_url(self, query: str) -> str:
        """
        converting search query into search url for AvaMovie

        param : query : user search query

        retrun : search link with qury

        example :
        input : 'spider man'
        retrun : 'https://avamovie3.info/?s=spider+man'
        """

        query = query.replace(" ", "+")
        return f"{AVAMOVIE_BASE_URL}/?s={query}"

    def search(self, query: str) -> dict[str, str]:
        """
        Requesting to search page with search query and extrac all results

        param : query : user search query

        retrun : dict of movie name and download page link

        example :
        input : 'amazing spider man'
        retrun :
        {
            'The Amazing Spider-Man 2012':'https://avamovie3.info/دانلود-فیلم-the-amazing-spider-man-2012/'
        }
        """
        
        results = list()
        self.url = self._create_search_url(query)
        self.scrap()

        results.extend(
            self.xpath("/html/body/main/div[2]/div/div[2]/article").css("h2.title a")
        )
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
            results.extend(
                self.xpath("/html/body/main/div[2]/div/div[2]/article").css(
                    "h2.title a"
                )
            )

        search_result: dict[str, str] = dict()

        for result in results:
            title = result.xpath("@title").get()
            link = result.xpath("@href").get()
            search_result[title] = link

        return search_result
