New project: > scrapy startproject tutorial

Terms: 
	Items - containers - scrapy.Item, scrapy.Field similar to ORM 
	Item Loaders - container loaders 
	Spiders - classes to scrape information - scrapy.Spider
		Need to define attributes (base:scrapy.Spider) 
			name - scraper name
			start_urls [url1,url2 ]  - to scrape
			allowed_domains [] - list of domains to allow 
			parse(self, response) - how to parse the response 
	Response object (spider.http.Respose) - created by Spider response 
	Selectors - XPath xpath('path') , CSS css('element'), Extract/extract(), re('regex') selectors 
	Shell mode - using ipython notebook 

Run Project: enter the spider to run dmoz_spider.py 
	scrapy crawl dmoz

FolderStructure: 
./tutorial/tutorial/__init__.py
./tutorial/tutorial/pipelines.py
./tutorial/scrapy.cfg

./tutorial/tutorial/settings.py

./tutorial/tutorial/items.py
	Example1: 
	class DmozItem(scrapy.Item):
		title = scrapy.Field()
		link = scrapy.Field()
		desc = scrapy.Field()
	Example2: 
	from scrapy.item import Item, Field
	class StackItem(Item):
	    title = Field()
	    url = Field()


./tutorial/tutorial/spiders/__init__.py
./tutorial/tutorial/spiders/dmoz_spider.py 
	Spider Example 1: 
	import scrapy

	class DmozSpider(scrapy.Spider):
	    name = "dmoz"
	    allowed_domains = ["dmoz.org"]
	    start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	    ]

	    def parse(self, response):
		filename = response.url.split("/")[-2] + '.html'
		with open(filename, 'wb') as f:
		    f.write(response.body)

	Spider Example 2: 
	from scrapy import Spider
	from scrapy.selector import Selector
	from stack.items import StackItem


	class StackSpider(Spider):
	    name = "stack"
	    allowed_domains = ["stackoverflow.com"]
	    start_urls = [
		"http://stackoverflow.com/questions?pagesize=50&sort=newest",
	    ]

	    def parse(self, response):
		questions = Selector(response).xpath('//div[@class="summary"]/h3')

		for question in questions:
		    item = StackItem()
		    item['title'] = question.xpath(
			'a[@class="question-hyperlink"]/text()').extract()[0]
		    item['url'] = question.xpath(
			'a[@class="question-hyperlink"]/@href').extract()[0]
		    yield item


