import inquirer  # type: ignore


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


def ask_with_options(options: list, question: str) -> str:
    questions = [
        inquirer.List(
            "option",
            message=question,
            choices=options,
        ),
    ]
    answers = inquirer.prompt(questions)

    return answers["option"]
