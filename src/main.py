from utils.banner import print_banner  # type: ignore
from utils.tools import ask_user_choice  # type: ignore


def main():
    print_banner()
    ask_user_choice()


if __name__ == "__main__":
    main()


# from spiders.download_links import DownloadLinksSpider   # type: ignore

# spider = DownloadLinksSpider("https://avamovie3.info/%d8%af%d8%a7%d9%86%d9%84%d9%88%d8%af-%d9%81%db%8c%d9%84%d9%85-the-amazing-spider-man-2-2014/")
# print(list(spider.get_download_links()))

# spider = SearchSpider()
# data = spider.search("spider man")

# for i in data:
#     print(i.css("h2.title a::attr(href)").extract()[0])
#     print(i.css("h2.title ::text").extract()[0])
