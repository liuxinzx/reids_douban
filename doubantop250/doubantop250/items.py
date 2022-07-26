# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Doubantop250Item(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    img_src = scrapy.Field()
    chinese_name = scrapy.Field()
    foreign_name = scrapy.Field()
    score = scrapy.Field()
    number_ratings = scrapy.Field()
    overview = scrapy.Field()
    details = scrapy.Field()
    pass
