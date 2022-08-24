import scrapy, json

class FindBestCategory(scrapy.spider):

    name = 'FindBEstCategory'
    list = []

    def start_requests(self):

        with open('categories.txt', 'r') as file:
            self.list = json.load(file)
