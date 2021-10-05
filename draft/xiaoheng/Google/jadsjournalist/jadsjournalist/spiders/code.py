import scrapy
from jadsjournalist.items import JadsjournalistItem
from datetime import datetime
import re

class Headlines(scrapy.Spider):
    name = 'test'


    def start_requests(self):
        urls = [
            'https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNRGxqTjNjd0VnSmxiaWdBUAE?hl=en-US&gl=US&ceid=US%3Aen',
            'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen',
            'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen', # Business
            'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen', # Technology
            'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen', # entertainments
            'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen', # sports
            'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen', #science
            'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen' # health
            #'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    #start_urls = [
    #    'https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNRGxqTjNjd0VnSmxiaWdBUAE?hl=en-US&gl=US&ceid=US%3Aen']  #

    def parse(self, response):

        for row in response.xpath("//h3[contains(@class, 'ipQwMb ekueJc RD0gLb')]"):
            item = JadsjournalistItem()
            item['title'] = row.xpath(".//a[contains(@class, 'DY5T1d RZIKme')]/text()").extract()

            item['cate'] = response.xpath("//div[contains(@class, 'xMjzl')]/h2[contains(@class,'OJMBqe')]//text()").extract()[0]
        # item['title'] = response.xpath(
        #     "//h3[contains(@class, 'ipQwMb ekueJc RD0gLb')]//a[contains(@class, 'DY5T1d RZIKme')]/text()").extract()
            yield item
    '''
    name = "journalists"
    allowed_domains = ['https://news.google.com/topics']
    # my urls
    start_urls = ['https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNRGxqTjNjd0VnSmxiaWdBUAE?hl=en-US&gl=US&ceid=US%3Aen']#, # US
    #               u'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen', # world
    #               u'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen', # Business
    #               u'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen', # Technology
    #               u'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen', # entertainments
    #               u'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen', # sports
    #               u'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen', #science
    #               u'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen' # health
    # )

    # def parse(self, start_urls):
    #     for url in start_urls:
    #         #url = "https:" + href.extract()
    #         yield scrapy.Request(url, callback=self.parse_dir_contents)
    def parse(self, response):
        item = JadsjournalistItem()

        #item['cate'] = response.xpath("//div[contains(@class, 'xMjzl')]/h2[contains(@class,'OJMBqe')]//text()").extract()[0]
        item['title'] = response.xpath("//h3[contains(@class, 'ipQwMb ekueJc RD0gLb')]//a[contains(@class, 'DY5T1d RZIKme')]/text()").extract()
        yield item
    '''