import requests  # type: ignore
from scrapy.selector import Selector, SelectorList  # type: ignore
from utils.typeshints import request_content  # type: ignore


class Scraper:
    def __init__(self, url) -> None:
        self.url = url
        self.request_content = None

    def scrap(self) -> request_content | None:
        req = requests.get(url=self.url)

        if req.status_code == 200:
            self.request_content = req.content
            return self.request_content

        raise ValueError(f"Recived {req.status_code} http status code from {self.url}")

    def css(self, query: str) -> SelectorList[Selector]:
        return Selector(text=self.request_content).css(query)

    def xpath(self, query: str) -> SelectorList[Selector]:
        return Selector(text=self.request_content).xpath(query)
