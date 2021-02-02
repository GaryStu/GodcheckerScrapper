import scrapy
import logging
from godchecker.items import GodItem

# mapping = {
#     "Name": "name",
#     "Pronunciation": "pronounciation",
#     "Alternative names": "",
#     "Gender": "",
#     "Type": "",
#     "Area or people": "",
#     "Celebration or Feast Day": "",
#     "In charge of": "",
#     "Area of expertise": "",
#     "Role": "",
#     "Good/Evil Rating": "",
#     "Popularity index": ""
# }
class GodSpider(scrapy.Spider):
    name = 'godchecker'

    start_urls = ['https://www.godchecker.com/']

    def parse(self, response):
        # TODO remove the duplicates for the first ones
        mythology_page_links = response.css('.pullout-panel li a')
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
        yield facts_and_figures

        

