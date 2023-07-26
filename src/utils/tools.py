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


def ask_user_choice():
    options = ["📡 Both", "🔎 Search movie name", "⬇️ Get a movie download links"]

    questions = [
        inquirer.List(
            "option",
            message="Select menu [Up & Down]",
            choices=options,
        ),
    ]
    answers = inquirer.prompt(questions)

    return answers["option"]
