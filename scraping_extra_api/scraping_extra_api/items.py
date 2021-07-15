# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
	id = scrapy.Field()
	url = scrapy.Field()
	title = scrapy.Field()
	sku = scrapy.Field()
	brand = scrapy.Field()
	categories = scrapy.Field()

class ReviewItem(scrapy.Item):
	id = scrapy.Field()
	product_id = scrapy.Field()
	product_sku = scrapy.Field()
	product_name = scrapy.Field()
	text = scrapy.Field()
	rating = scrapy.Field()
	date = scrapy.Field()
	dislikes = scrapy.Field()
	likes = scrapy.Field()