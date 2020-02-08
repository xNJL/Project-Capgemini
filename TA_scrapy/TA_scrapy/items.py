# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

import pandas as pd


class XActuItem(scrapy.Item):
    titre_article = scrapy.Field()
    lien_article = scrapy.Field()
    date_article = scrapy.Field()
    content = scrapy.Field()
    related_subject = scrapy.Field()
    related_subject_links = scrapy.Field()



class ReviewRestoItem(scrapy.Item):
        
    Date_of_visit = scrapy.Field()
    Restaurant_name=scrapy.Field()
    Review_title = scrapy.Field()
    Review = scrapy.Field()
    Rating = scrapy.Field()
    Review_url=scrapy.Field()
