from spiders.download_links import DownloadLinksSpider  # type: ignore
from spiders.search import SearchSpider  # type: ignore

from utils.banner import print_banner  # type: ignore
from utils.tools import ask_with_options, clear_terminal_screen  # type: ignore
import settings  # type: ignore
from rich import print


def search_movie():
    query = input("Enter movie name: ")
    spider = SearchSpider()
    search_results = spider.search(query=query)
    clear_terminal_screen()
    print("Result Count: ", len(search_results))
    seleceted = ask_with_options(
        options=search_results.keys(),
        question=settings.SEARCH_SELECET_QUESTION,
    )
    return search_results[seleceted]


def get_moive_download_links(page_url=None):
    if not page_url:
        page_url = input("Enter movie page url: ")

    spider = DownloadLinksSpider(page_url)
    results = spider.get_download_links()
    for quality, link in results:
        print(f":star: {quality} => {link}")


def main():
    user_choice = ask_with_options(
        options=settings.USER_CHOICES, question=settings.START_MENU_QUESTION
    )

    if user_choice == settings.USER_CHOICE_BOTH:
        movie_page_link = search_movie()
        get_moive_download_links(movie_page_link)

    elif user_choice == settings.USER_CHOICE_SEARCH_MOIVE:
        result = search_movie()
        print("Movie Page link: ", result)

    elif user_choice == settings.USER_CHOICE_GET_DOWNLOAD_LINK:
        get_moive_download_links()


if __name__ == "__main__":
    clear_terminal_screen()
    print_banner()
    main()
