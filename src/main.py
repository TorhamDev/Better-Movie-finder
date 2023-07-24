import inquirer

options = ["🔎 Search movie name", "⬇️ Get a movie download links", "📡 Both"]

questions = [
    inquirer.List(
        "option",
        message="Select menu",
        choices=options,
    ),
]
answers = inquirer.prompt(questions)

print(answers)
print(answers["option"])


# from spiders.search import SearchSpider

# spider = SearchSpider()
# data = spider.search("spider man")

# for i in data:
#     print(i.css("h2.title a::attr(href)").extract()[0])
#     print(i.css("h2.title ::text").extract()[0])
