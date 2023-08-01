from scraper import Scraper  # type: ignore
from utils.tools import clean_text  # type: ignore


class DownloadLinksSpider(Scraper):
    """
    This spider requests the movie download page and extracts the download links
    """

    def __init__(self, url) -> None:
        self.url = url
        self.scrap()

    def get_download_links(self):
        """
        Extracting download link for the movie download page

        return : zip object
        [(quality, link)]

        example return :
        [('Bluray 1080p', 'https://download.link/the.movie.mkv')]
        """
        download_links = self.css("div.row_data")

        links = []
        qualities = []
        for link in download_links:
            m_link = (
                link.css("a.siteSingle__boxContent__downloadContent__link")
                .xpath("@href")
                .get()
            )
            m_quality = clean_text(link.css("div.quality *::text").get())
            links.append(m_link)
            qualities.append(m_quality)

        return zip(filter(None, qualities), filter(None, links))
