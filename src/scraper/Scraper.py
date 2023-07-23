import requests  # type: ignore
from scrapy.selector import Selector  # type: ignore


class Scraper:
    def __init__(self, url) -> None:
        self.url = url
        self.request_content = None

    def scrap(self):
        req = requests.get(url=self.url)

        if req.status_code == 200:
            req.content

        raise ValueError(f"Recived {req.status_code} http status code from {self.url}")

    def css(self, css_query: str):
        return Selector(text=self.request_content).css(css_query)

    def xpath(self, xpath_query: str):
        return Selector(text=self.request_content).xpath(xpath_query)
