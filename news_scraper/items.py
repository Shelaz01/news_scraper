# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsArticleItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    text = scrapy.Field()
    source = scrapy.Field()
    date = scrapy.Field()
