import scrapy, json

class getCategories(scrapy.Spider):

    name = 'getCategories'

    start_urls = ["https://www.amazon.com/"]

    def parse(self, response):

        list = response.css('#searchDropdownBox > option::attr(value)').getall()

        with open("categories.txt", 'w') as file:
            json.dump(list, file)
