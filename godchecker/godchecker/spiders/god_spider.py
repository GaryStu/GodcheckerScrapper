import scrapy
import logging
from scrapy.loader import ItemLoader
from godchecker.items import GodItem

# Mapping between the scrapped str and the table attributes
rename_mapping = {
    "Name": "name",
    "Pronunciation": "pronounciation",
    "Alternative names": "alt_names",
    "Gender": "gender",
    "Type": "type",
    "Area or people": "area_or_people",
    "Celebration or Feast Day": "celeb_or_feast_day",
    "In charge of": "in_charge_of",
    "Area of expertise": "area_of_expertise",
    "Role": "role",
    "Good/Evil Rating": "good_evil",
    "Popularity index": "popularity_index",
    "Birth and Death Dates": "birth_death_dates"
}
class GodSpider(scrapy.Spider):
    name = 'godchecker'

    start_urls = ['https://www.godchecker.com/']

    def parse(self, response):
        # TODO remove the duplicates for the first ones
        mythology_page_links = response.css('#pantheon-list .pullout-panel:not(:first-child) a')
        yield from response.follow_all(mythology_page_links, self.parse_mythology)

    def parse_mythology(self, response):
        pantheons_page_link = response.css('#leftbar a')[1]
        yield response.follow(pantheons_page_link, self.parse_pantheon)
    
    def parse_pantheon(self, response):
        god_page_links = response.css('.search-result a')
        yield from response.follow_all(god_page_links, self.parse_god)

    def parse_god(self, response):
        attributes = [attr.strip()[:-1] for attr in response.css('div.pullout-panel.vitalsbox p::text').getall() if len(attr.strip()) > 0]
        values = response.css('div.pullout-panel strong::text').getall()
        facts_and_figures = dict(zip(attributes, values))

        loader = ItemLoader(item=GodItem(), response=response)
        for key, value in facts_and_figures.items():
            logging.debug(f'{key} -> {value}')
            rename = rename_mapping[key]
            logging.debug(f'rename: {key} -> {rename}')
            loader.add_value(rename_mapping[key], value)
        
        
        yield loader.load_item()