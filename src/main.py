from spiders.download_links import DownloadLinksSpider  # type: ignore
from spiders.search import SearchSpider  # type: ignore

from utils.banner import print_banner  # type: ignore
from utils.tools import ask_with_options  # type: ignore
import settings  # type: ignore


def main():
    print_banner()
    user_choice = ask_with_options(
        options=settings.USER_CHOICES, question=settings.START_MENU_QUESTION
    )

    if user_choice == settings.USER_CHOICE_BOTH:
        ...
    elif user_choice == settings.USER_CHOICE_SEARCH_MOIVE:
        query = input("Enter movie name: ")
        spider = SearchSpider()
        search_results = spider.search(query=query)
        print("Result Count: ", len(search_results))
        seleceted = ask_with_options(
            options=search_results.keys(), question=settings.SEARCH_SELECET_QUESTION
        )
        print("Movie Page link: ", search_results[seleceted])

    elif user_choice == settings.USER_CHOICE_GET_DOWNLOAD_LINK:
        ...


if __name__ == "__main__":
    main()


# from spiders.download_links import DownloadLinksSpider   # type: ignore

# spider = DownloadLinksSpider("https://avamovie3.info/%d8%af%d8%a7%d9%86%d9%84%d9%88%d8%af-%d9%81%db%8c%d9%84%d9%85-the-amazing-spider-man-2-2014/")
# print(list(spider.get_download_links()))
