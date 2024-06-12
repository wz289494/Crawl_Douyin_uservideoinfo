# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyinuserItem(scrapy.Item):
    video_name = scrapy.Field()

    video_url = scrapy.Field()

    video_like = scrapy.Field()

