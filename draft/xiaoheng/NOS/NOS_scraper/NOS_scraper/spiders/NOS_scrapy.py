import scrapy
#from NOS_scraper.items import NosScraperItem

class NosScrapySpider(scrapy.Spider):
    name = 'NOS_scrapy'
    allowed_domains = ['https://nos.nl/nieuws/economie']
    start_urls = ['http://nos.nl/nieuws/economie']
###response.xpath("//div[contains(@class, 'list-items__content link-reset')]/h3[contains(@
#class, 'list-items__title list-items__link-hover')]/text()").extract()



    def parse(self, response):
        #item = NosScraperItem()

        #item['title'] = response.xpath("//div[contains(@class, 'list-items__content link-reset')]/h3[contains(@class, 'list-items__title list-items__link-hover')]/text()").extract()
        #yield item
        for row in response.xpath("//div[contains(@class, 'list-items__content link-reset')]"):
            title = row.xpath("./h3[contains(@class, 'list-items__title list-items__link-hover')]/text()").extract()
            time = row.xpath(".//div[contains(@class, 'list-items__meta')]/time[contains(@class, 'list-items__time')]//@datetime").extract()
            yield {
                'title': title,
                'time':time
            }

        pass
'''
response.xpath("//div[contains(@class, 'list-items__content link-reset')]//div[contains
(@class, 'list-items__meta')]/time[contains(@class, 'list-items__time')]//@datetime").extra
ct()
'''