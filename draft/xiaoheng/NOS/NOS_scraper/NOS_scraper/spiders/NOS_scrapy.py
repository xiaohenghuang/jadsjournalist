import scrapy


class NosScrapySpider(scrapy.Spider):
    name = 'NOS_scrapy'
    allowed_domains = ['https://nos.nl/nieuws']
    start_urls = ['http://https://nos.nl/nieuws/']

    def parse(self, response):
        pass
