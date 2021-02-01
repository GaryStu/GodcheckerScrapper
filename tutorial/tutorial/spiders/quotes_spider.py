import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    # Instead of implementing a start_requests() use start_urls
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]
    
    # Must return an iterable of Requests
    # You can either ereutnr a list of requests or write a generator function
    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        # Parse the response, extracting the scraped data as dicts and finding new URLs to follow
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            # When you yield a Request in a callback method, Scrapy will schedule that request
            # to be sent and register a callback method to be exectued when that request finishes
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

            # Shortcut using response.follow
            # yield response.follow(next_page, callback=self.parse)

        # Another way
        # for href in response.css('ul.pager a::attr(href)'):
        #     yield response.follow(href, callback=self.parse)

        # Another shorter way for <a> element
        # for a in response.css('ul.pager a'):
        #     yield response.follow(a, callback=self.parse)

        # Create multiple requests from an iterable, use follow_all
        # anchors = response.css('ul.pager a')
        # yield from response.follow_all(anchors, callback=self.parse)

        # Shortening it further
        # yield from response.follow_all(css='ul.pager a', callback=self.parse)


        # Get the whole page
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')
    
