import requests  # type: ignore


class Scraper:
    def __init__(self, url) -> None:
        self.url = url

    def scrap(self):
        req = requests.get(url=self.url)

        if req.status_code == 200:
            req.content

        raise ValueError(f"Recived {req.status_code} http status code from {self.url}")
