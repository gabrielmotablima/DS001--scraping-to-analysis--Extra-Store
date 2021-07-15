# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy import settings
from scrapy.exceptions import DropItem
# from scrapy import log

class MongoDBPipeline:
	def __init__(self):
	    connection = pymongo.MongoClient('localhost', 27017)
	    db = connection["db_scraping_extra"]
	    self.collection_products = db["products"]
	    self.collection_reviews = db["reviews"]

	def process_item(self, item, spider):
		valid = True
		for data in item:
			if not data:
				valid = False
				raise DropItem("Missing {0}!".format(data))
		if valid:
			if 'sku' in dict(item):
				try:
					self.collection_products.insert(dict(item))
					print(f'Product "{item["title"]}" was added to MongoDB database!')
				except:
					print("Failed in product insertion.")
			else:
				try:
					self.collection_reviews.insert(dict(item))
					print(f"Review was added to MongoDB database!")
				except:
					print("Failed in review insertion.")
		return item
    # def process_item(self, item, spider):
    #     return item
