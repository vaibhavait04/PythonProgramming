# Scrapy notes 

## New project
 > scrapy startproject tutorial

## Terms: 
*	Items - containers - scrapy.Item, scrapy.Field similar to ORM 
*	Item Loaders - container loaders 
*	Spiders - classes to scrape information - scrapy.Spider
*		Need to define attributes (base:scrapy.Spider) 
		>	name - scraper name
		>	start_urls [url1,url2 ]  - to scrape
		>	allowed_domains [] - list of domains to allow 
		>	parse(self, response) - how to parse the response 
*	Response object (spider.http.Respose) - created by Spider response 
*	Selectors - XPath xpath('path') , CSS css('element'), Extract/extract(), re('regex') selectors 
*	Pipeline - to process the items - used for DB storage 
	Sample source code with Pipeline: https://github.com/realpython/stack-spider/releases/tag/v2

*	Shell mode - using ipython notebook 
		scrapy shell "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"
			'response' variable will have all the data 
	>		response.xpath('//title') , response.xpath('//title/text()').extract() 
	>		response.xpath('//title').re('(\w+)')  
	>		response.css(), response
	>		for sel in response.xpath('//ul/li'):
	>			title = sel.xpath('a/text()').extract()
	>			link = sel.xpath('a/@href').extract()
	>			desc = sel.xpath('text()').extract()
	>			print title, link, desc
	
* Run Project: enter the spider to run dmoz_spider.py 
	> scrapy crawl dmoz

* FolderStructure: 
> ./tutorial/tutorial/__init__.py
> ./tutorial/scrapy.cfg

> ./tutorial/tutorial/settings.py
	settings for mongodb: 
		ITEM_PIPELINES = ['stack.pipelines.MongoDBPipeline', ]
		MONGODB_SERVER = "localhost"
		MONGODB_PORT = 27017
		MONGODB_DB = "stackoverflow"
		MONGODB_COLLECTION = "questions"
		DOWNLOAD_DELAY = 5
> ./tutorial/tutorial/items.py
*	Example1: 
	class DmozItem(scrapy.Item):
		title = scrapy.Field()
		link = scrapy.Field()
		desc = scrapy.Field()
*	Example2: 
	from scrapy.item import Item, Field
	class StackItem(Item):
	    title = Field()
	    url = Field()


> ./tutorial/tutorial/spiders/__init__.py
> ./tutorial/tutorial/spiders/dmoz_spider.py 

* Spider Example 1: 

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

* Spider Example 2: 

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

* DMOZ to follow links as well: 

	import scrapy

	from tutorial.items import DmozItem

	class DmozSpider(scrapy.Spider):
	    name = "dmoz"
	    allowed_domains = ["dmoz.org"]
	    start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/",
	    ]

	    def parse(self, response):
		for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
		    url = response.urljoin(href.extract())
		    yield scrapy.Request(url, callback=self.parse_dir_contents)

	    def parse_dir_contents(self, response):
		for sel in response.xpath('//ul/li'):
		    item = DmozItem()
		    item['title'] = sel.xpath('a/text()').extract()
		    item['link'] = sel.xpath('a/@href').extract()
		    item['desc'] = sel.xpath('text()').extract()
		    yield item

* DMOZ - recursive calling the web page links - Loop through pages 

	def parse_articles_follow_next_page(self, response):
	    for article in response.xpath("//article"):
		item = ArticleItem()

		... extract article data here

		yield item

	    next_page = response.css("ul.navigation > li.next-page > a::attr('href')")
	    if next_page:
		url = response.urljoin(next_page[0].extract())
		yield scrapy.Request(url, self.parse_articles_follow_next_page)

* DMOZ - passing additional information to the callbacks - use request.meta['item'] = value 

	def parse_page1(self, response):
	    item = MyItem()
	    item['main_url'] = response.url
	    request = scrapy.Request("http://www.example.com/some_page.html",
				     callback=self.parse_page2)
	    request.meta['item'] = item   # <<-- 
	    return request

	def parse_page2(self, response):
	    item = response.meta['item']   # <<-- 
	    item['other_url'] = response.url
	    return item

* Storing to DB - mongodb : Using Pipeline 
> ./tutorial/tutorial/pipelines.py
pipeline.py 
	import pymongo

	from scrapy.conf import settings
	from scrapy.exceptions import DropItem
	from scrapy import log


	class MongoDBPipeline(object):

	    def __init__(self):
		connection = pymongo.MongoClient(
		    settings['MONGODB_SERVER'],
		    settings['MONGODB_PORT']
		)
		db = connection[settings['MONGODB_DB']]
		self.collection = db[settings['MONGODB_COLLECTION']]

	    def process_item(self, item, spider):
		valid = True
		for data in item:
		    if not data:
			valid = False
			raise DropItem("Missing {0}!".format(data))
		if valid:
		    self.collection.insert(dict(item))
		    log.msg("Question added to MongoDB database!",
			    level=log.DEBUG, spider=spider)
		return item


