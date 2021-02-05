# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from typing import Optional

# native-american-mythology -> "native american"
def parse_mythology(text):
    splitText = text.split('-')
    delimiter = " "
    return delimiter.join(splitText[0:-1])

class GodItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    name = Field(
        output_processor=TakeFirst()
    )
    mythology = Field(
        input_processor=MapCompose(parse_mythology),
        output_processor=TakeFirst()
    )
    pronounciation = Field(
        output_processor=TakeFirst()
    )
    alt_names = Field(
        output_processor=TakeFirst()
    )
    gender = Field(
        output_processor=TakeFirst()
    )
    type = Field(
        output_processor=TakeFirst()
    )
    area_or_people = Field(
        output_processor=TakeFirst()
    )
    celeb_or_feast_day = Field(
        output_processor=TakeFirst()
    )
    in_charge_of : Optional[str]= Field(
        default=None, 
        output_processor=TakeFirst()
    )
    area_of_expertise = Field(
        output_processor=TakeFirst()
    )
    role = Field(
        output_processor=TakeFirst()
    )
    good_evil = Field(
        output_processor=TakeFirst()
    )
    popularity_index = Field(
        output_processor=TakeFirst()
    )
    birth_death_dates = Field(
        output_processor=TakeFirst()
    )
