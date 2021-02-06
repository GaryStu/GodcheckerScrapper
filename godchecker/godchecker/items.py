# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from typing import Optional

# e.g. native-american-mythology -> "native american"
def parse_mythology(text):
    splitText = text.split('-')
    delimiter = " "
    return delimiter.join(splitText[0:-1])

def parse_alt_names(text):
    if len(text) == 0: 
        return None
    return text

def parse_pronounciation(text):
    if text == 'Coming soon' or text == "Sorry, we don't know":
        return None
    return text

def parse_gender(text):
    if len(text) == 0 or text == "Sorry, we don't know":
        return None
    return text

def parse_type(text):
    if text == "Sorry, we don't know":
        return None
    return text

def parse_area_or_people(text):
    if text == 'Coming soon':
        return None
    return text

def parse_celeb_or_feast_day(text):
    if text == 'Unknown at present':
        return None
    return text

def parse_in_charge_of(text):
    if len(text) == 0 or text == 'Unknown':
        return None
    return text

def parse_area_of_expertise(text):
    if len(text) == 0 or text == 'Unknown':
        return None
    return text

def parse_role(text):
    if len(text) == 0 or text == 'Unknown at present':
        return None
    return text

def parse_good_evil(text):
    if text == 'good_evil' or text == 'Unknown at present':
        return None
    return text.split(',')[0]

def parse_birth_death_dates(text):
    if len(text) == 0:
        return None
    return text

def parse_name_meaning(text):
    if len(text) == 0:
        return None
    return text

def parse_associated_with(text):
    if len(text) == 0:
        return None
    return text


class GodItem(Item):
    name = Field(
        output_processor=TakeFirst()
    )
    mythology = Field(
        input_processor=MapCompose(parse_mythology),
        output_processor=TakeFirst()
    )
    pronounciation = Field(
        input_processor=MapCompose(parse_pronounciation),
        output_processor=TakeFirst()
    )
    alt_names = Field(
        input_processor=MapCompose(parse_alt_names),
        output_processor=TakeFirst()
    )
    gender = Field(
        input_processor=MapCompose(parse_gender),
        output_processor=TakeFirst()
    )
    type = Field(
        input_processor=MapCompose(parse_type),
        output_processor=TakeFirst()
    )
    area_or_people = Field(
        input_processor=MapCompose(parse_area_or_people),
        output_processor=TakeFirst()
    )
    celeb_or_feast_day = Field(
        input_processor=MapCompose(parse_celeb_or_feast_day),
        output_processor=TakeFirst()
    )
    in_charge_of : Optional[str]= Field(
        input_processor=MapCompose(parse_in_charge_of),
        default=None, 
        output_processor=TakeFirst()
    )
    area_of_expertise = Field(
        input_processor=MapCompose(parse_area_of_expertise),
        output_processor=TakeFirst()
    )
    role = Field(
        input_processor=MapCompose(parse_role),
        output_processor=TakeFirst()
    )
    good_evil = Field(
        input_processor=MapCompose(parse_good_evil),
        output_processor=TakeFirst()
    )
    popularity_index = Field(
        output_processor=TakeFirst()
    )
    birth_death_dates = Field(
        input_processor=MapCompose(parse_birth_death_dates),
        output_processor=TakeFirst()
    )
    name_meaning = Field(
        input_processor=MapCompose(parse_name_meaning),
        output_processor=TakeFirst()
    )
    associated_with = Field(
        input_processor=MapCompose(parse_associated_with),
        output_processor=TakeFirst()
    )
