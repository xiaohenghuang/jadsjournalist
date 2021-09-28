import scrapy
from fundrazr.items import GoogleItem
import re

class Google(scrapy.Spider):
    name = "my_scraper"
    start_urls = ['https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen']

    def parse(self, response):
        item = GoogleItem()
        item['newsTitle'] = response.xpath("//h3[contains(@class, 'ipQwMb ekueJc RD0gLb')]/a[contains(@class, 'DY5T1d RZIKme')]/text()").extract()
        yield item
        # for title in response.xpath("//h3[contains(@class, 'ipQwMb ekueJc RD0gLb')]/a[contains(@class, 'DY5T1d RZIKme')]/text()"):
        #     # add the scheme, eg http://
        #     title_ls = "https:" + title.extract()
        #     yield scrapy.Request(title_ls, callback=self.parse_dir_contents)



'''
import scrapy
from fundrazr.items import FundrazrItem
from datetime import datetime
import re


class Fundrazr(scrapy.Spider):
	name = "my_scraper"

	# First Start Url
	start_urls = ["https://fundrazr.com/find?category=Health"]

	npages = 2

	# This mimics getting the pages using the next button.
	for i in range(2, npages + 2):
		start_urls.append("https://fundrazr.com/find?category=Health&page="+str(i)+"")

	def parse(self, response):
		for href in response.xpath("//h2[contains(@class, 'title headline-font')]/a[contains(@class, 'campaign-link')]//@href"):
			# add the scheme, eg http://
			url  = "https:" + href.extract()
			yield scrapy.Request(url, callback=self.parse_dir_contents)

	def parse_dir_contents(self, response):
		item = FundrazrItem()

		# Getting Campaign Title
		item['campaignTitle'] = response.xpath("//div[contains(@id, 'campaign-title')]/descendant::text()").extract()[0].strip()

		# Getting Amount Raised
		item['amountRaised']= response.xpath("//span[contains(@class, 'stat')]/span[contains(@class, 'amount-raised')]/descendant::text()").extract()

		# Goal
		item['goal'] = " ".join(response.xpath("//div[contains(@class, 'stats-primary with-goal')]//span[contains(@class, 'stats-label hidden-phone')]/text()").extract()).strip()

		# Currency Type (US Dollar Etc)
		item['currencyType'] = response.xpath("//div[contains(@class, 'stats-primary with-goal')]/@title").extract()

		# Campaign End (Month year etc)
		item['endDate'] = "".join(response.xpath("//div[contains(@id, 'campaign-stats')]//span[contains(@class,'stats-label hidden-phone')]/span[@class='nowrap']/text()").extract()).strip()

		# Number of contributors
		item['numberContributors'] = response.xpath("//div[contains(@class, 'stats-secondary with-goal')]//span[contains(@class, 'donation-count stat')]/text()").extract()

		# Getting Story
		story_list = response.xpath("//div[contains(@id, 'full-story')]/descendant::text()").extract()
		story_list = [x.strip() for x in story_list if len(x.strip()) > 0]
		item['story']  = " ".join(story_list)

		# Url (The link to the page)
		item['url'] = response.xpath("//meta[@property='og:url']/@content").extract()

		yield item
'''