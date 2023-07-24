from spiders.search import SearchSpider

spider = SearchSpider()
data = spider.search("amazing spider man")

for i in data:
    print(i.css("h2.title a::attr(href)").extract()[0])
    print(i.css("h2.title ::text").extract()[0])