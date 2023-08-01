import sys
from rich import print as r_print
from rich.prompt import Prompt
from spiders.download_links import DownloadLinksSpider  # type: ignore
from spiders.search import SearchSpider  # type: ignore
from utils.banner import print_banner, columns as terminal_columns  # type: ignore
from utils.tools import ask_with_options, clear_terminal_screen  # type: ignore
import settings  # type: ignore


def search_movie():
    """
    Searching process form  getting search input to finding movie download page

    return : movie download link
    """
    query = Prompt.ask(":movie_camera: Enter movie name")
    spider = SearchSpider()
    search_results = spider.search(query=query)
    clear_terminal_screen()

    if len(search_results) == 0:
        r_print("\n", "Nothing found :cry:".center(terminal_columns), "\n")
        sys.exit()

    r_print(
        "\n",
        f":sparkles: :cake: [red]Result Count:[/red] {len(search_results)}:sparkles:".center(
            terminal_columns
        ),
        "\n",
    )

    selected = ask_with_options(
        options=search_results.keys(),
        question=settings.SEARCH_SELECT_QUESTION,
    )
    return search_results[selected]


def get_movie_download_links(page_url=None):
    """
    Process of extracting movie download links from movie download page

    param : page_url : movie download page

    and then print all download links with quality
    example :

    :star: Bluray 1080p => https://download.movie.link/1080p.mkv
    :star: Bluray 720p => https://download.movie.link/720.mkv
    """
    if not page_url:
        page_url = Prompt.ask(":movie_camera: Enter movie page url")

    spider = DownloadLinksSpider(page_url)
    results = spider.get_download_links()
    for quality, link in results:
        r_print(f":star: {quality} => {link}")


def main():
    """
    script main
    """
    user_choice = ask_with_options(
        options=settings.USER_CHOICES, question=settings.START_MENU_QUESTION
    )

    if user_choice == settings.USER_CHOICE_BOTH:
        movie_page_link = search_movie()
        get_movie_download_links(movie_page_link)

    elif user_choice == settings.USER_CHOICE_SEARCH_MOVIE:
        result = search_movie()
        r_print(":smiling_imp: Movie Page link: ", result)

    elif user_choice == settings.USER_CHOICE_GET_DOWNLOAD_LINK:
        get_movie_download_links()


if __name__ == "__main__":
    clear_terminal_screen()
    print_banner()
    main()
