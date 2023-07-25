from scraper import Scraper  # type: ignore
from utils.tools import clean_text  # type: ignore


class DownloadLinksSpider(Scraper):
    def __init__(self, url) -> None:
        self.url = url
        self.scrap()

    def get_download_links(self):
        download_links = self.css("div.row_data")

        links = []
        qualites = []
        for link in download_links:
            m_link = (
                link.css("a.siteSingle__boxContent__downloadContent__link")
                .xpath("@href")
                .get()
            )
            m_quality = clean_text(link.css("div.quality *::text").get())
            links.append(m_link)
            qualites.append(m_quality)

        return zip(filter(None, qualites), filter(None, links))
