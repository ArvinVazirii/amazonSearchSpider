import scrapy, json, urllib.parse, time, operator
from urllib.error import HTTPError

class FindBestCategory(scrapy.Spider):

    name = 'FindBestCategory'
    list = []
    besturl = {}

    site_url = 'https://www.amazon.com/'
    searchurl = 's?k='
    specifyurl = '&i='

    def start_requests(self):

        name = input('What you want to search for: ')

        with open('categories.txt', 'r') as file:
            self.list = json.load(file)

        url = self.site_url + self.searchurl + urllib.parse.quote_plus(name, safe = '') + self.specifyurl

        with open('log.txt', 'w') as file:
            json.dump(name, file)

        for i in self.list:

            while True:
                try:
                    yield scrapy.Request(url + i[i.find('=') + 1:], callback = self.parse)
                    break
                except HTTPError as e:
                    print('Rid')



    def parse(self, response):


        pagecount = response.css('.s-pagination-ellipsis+ .s-pagination-disabled::text').get()
        print(pagecount)

        if pagecount is not None:
            self.besturl[response.url] = int(pagecount)

        else:
            self.besturl[response.url] = 0


    def closed(self, reason):

        self.besturl = dict(sorted(self.besturl.items(), key = operator.itemgetter(1), reverse = True))

        with open('infos.txt', 'w') as file:
            json.dump(self.besturl, file)
