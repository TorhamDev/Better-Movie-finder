import inquirer  # type: ignore
from settings import USER_CHOICES


def clean_text(text: str) -> str:
    if text:
        return (
            text.replace("\t", "")
            .replace("\u200e", " ")
            .replace("\u200c", " ")
            .replace("\n", " ")
            .replace("\r", " ")
        )
    return text


def ask_user_choice() -> str:
    options = USER_CHOICES

    questions = [
        inquirer.List(
            "option",
            message="Select menu [Up & Down]",
            choices=options,
        ),
    ]
    answers = inquirer.prompt(questions)

    return answers["option"]
