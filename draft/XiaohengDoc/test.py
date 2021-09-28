start_urls = ["https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"]
#scrapy shell "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"

#response.xpath("//h3[contains(@class, 'ipQwMb ekueJc RD0gLb')]/a[contains(@class, 'DY5T1d RZIKme')]/text()").extract()
for href in response.xpath("//h3[contains(@class, 'ipQwMb ekueJc RD0gLb')]/a[contains(@class, 'DY5T1d RZIKme')]/text()"):
	# add the scheme, eg http://
	url  = "https:" + href.extract()