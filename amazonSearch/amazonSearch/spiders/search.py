import scrapy, json, urllib.parse, time

class search(scrapy.Spider):

    name = 'search'

    site_url = 'https://www.amazon.com/'
    searchurl = 's?k='
    specifyurl = '&i='

    def start_requests(self):

        name = input('what you want to search for :')
        with open('categories.txt', 'r') as file:
            list = json.load(file)

        for i in list:
            url = self.site_url + self.searchurl + urllib.parse.quote_plus(name, safe = '') + self.specifyurl + i[i.find('=') + 1:]
            yield scrapy.Request(url, callback = self.parse)
            # time.sleep(2)

    def parse(self, response):

        namelist = response.css('.a-size-base-plus::text').getall()
        for i in namelist:
            yield {'name' : i}

        nextpage = response.css('.s-pagination-next::attr(href)').get()


        if nextpage is not None:
            # nextpage = response.urljoin(nextpage)
            # yield scrapy.Request(nextpage, callback = self.parse)
            yield response.follow(nextpage, callback = self.parse)
            # time.sleep(1)
