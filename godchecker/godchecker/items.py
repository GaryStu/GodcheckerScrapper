# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class GodItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    name = Field()
    pronounciation = Field()
    alt_names = Field()
    gender = Field()
    type = Field()
    area_or_people = Field()
    celeb_or_feast_day = Field()
    in_charge_of = Field()
    area_of_expertise = Field()
    role = Field()
    good_evil = Field()
    popularity_index = Field()
