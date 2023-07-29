import inquirer  # type: ignore
from os import system
from platform import platform


def clean_text(text: str) -> str:
    """
    Clear whitespace and extra chars from text
    """
    if text:
        return (
            text.replace("\t", "")
            .replace("\u200e", " ")
            .replace("\u200c", " ")
            .replace("\n", " ")
            .replace("\r", " ")
        )
    return text


def ask_with_options(options: list, question: str) -> str:
    """
    Create a ask menu with inquirer lib

    param : options : list of option in menu
    param : question : question for showing to user

    return : user answer/select
    """
    questions = [
        inquirer.List(
            "option",
            message=question,
            choices=options,
        ),
    ]
    answers = inquirer.prompt(questions)

    return answers["option"]


def clear_terminal_screen() -> None:
    """
    clearing terminal by running clear in linux and mac. and cls in windows
    """

    running = platform()

    if "Windows" in running:
        system("cls")

    elif "Linux" in running:
        system("clear")

    elif "macOS" in running:
        system("clear")
