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
    id_resto = scrapy.Field()
    id_comment = scrapy.Field()
    resto = scrapy.Field()
    resto_url = scrapy.Field()
    rating = scrapy.Field()
    title = scrapy.Field()
    diner_date = scrapy.Field()
    rating_date = scrapy.Field()
    answer_text = scrapy.Field()
    reviewer_pseudo = scrapy.Field()
    reviewer_origin = scrapy.Field()
    reviewer_info_sup = scrapy.Field()
    other_ratings_category = scrapy.Field()
    other_ratings_value = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()


class RestoItem(scrapy.Item):
    url = scrapy.Field()
    id = scrapy.Field()
    name_url = scrapy.Field()
    titre = scrapy.Field()
    rating = scrapy.Field()
    nb_review = scrapy.Field()
    street_adress = scrapy.Field()
    locality = scrapy.Field()
    country = scrapy.Field()
    tel_number = scrapy.Field()
    # tel_number2 = scrapy.Field()
    url_menu = scrapy.Field()
    info_1 = scrapy.Field()
    info_2 = scrapy.Field()
    price_range = scrapy.Field()
    picture_number = scrapy.Field()
    avg_rating = scrapy.Field()
    nb_reviews = scrapy.Field()
    local_ranking = scrapy.Field()
    other_information = scrapy.Field()
    all_rankings = scrapy.Field()
    categories_ranking = scrapy.Field()
    description = scrapy.Field()
    details = scrapy.Field()
    rating_excellent = scrapy.Field()
    rating_very_good = scrapy.Field()
    rating_average = scrapy.Field()
    rating_poor = scrapy.Field()
    rating_terrible = scrapy.Field()
