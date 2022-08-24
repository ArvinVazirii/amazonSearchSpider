# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AmazonsearchPipeline:
    count = 0

    def close_spider(self, spider):

        with open("log.txt", 'w') as file:
            file.write(str(self.count))

    def process_item(self, item, spider):
        self.count += 1
        return item
