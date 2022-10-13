import scrapy, json, urllib.parse, time
from urllib.error import HTTPError

class search(scrapy.Spider):

    name = 'search'

    # site_url = 'https://www.amazon.com/'

    urlinfos = {}
    searchfor = ''

    def start_requests(self):

        with open('infos.txt', 'r') as file:
            self.urlinfos = json.load(file)


        yield scrapy.Request(list(self.urlinfos.items())[0][0], callback = self.parse)
            
    def parse(self, response):

        namelist = response.css('.a-size-base-plus::text').getall()
        for i in namelist:
            yield {'name' : i}

        nextpage = response.css('.s-pagination-next::attr(href)').get()


        if nextpage is not None:
            while True:
                try:
                    yield response.follow(nextpage, callback = self.parse)
                    break
                except HTTPError as e:
                    print('Ridi')
