import scrapy
import json

from scraping_extra_api.items import ProductItem, ReviewItem

import time
import random

class CoolersSpider(scrapy.Spider):
	filters = { 'coolers' : 'c13_c14_c13' }
	page_products = 1

	name = 'coolers'
	allowed_domains = ['www.extra.com.br', 'pdp-api.extra.com.br']
	start_urls = [f'http://www.extra.com.br/api/catalogo-ssr/products/?Filtro={filters["coolers"]}&PaginaAtual={page_products}']

	page_reviews = 0
	empty_review = False
	product_model = {
		'id': 0,
		'title': '',
		'sku': 0
		}

	products = product_model
	item_product = ProductItem()
	item_review = ReviewItem()


	def parse(self, response):
		data = json.loads(response.text)

		if data['products']:
			for product in data["products"]:

				self.page_reviews = 0
				self.empty_review = False

				sku = ''
				url_string = product['urls']

				for i in url_string[::-1]:
					if i != '/':
						sku = i + sku
					else:
						break

				self.item_product['id'] = product['id']
				self.item_product['url'] = product['urls']
				self.item_product['title'] = product['name']
				self.item_product['sku'] = int(sku)
				self.item_product['brand'] = product['brand']
				self.item_product['categories'] = product['categories']

				yield self.item_product

				self.products['id'] = product['id']
				self.products['title'] = product['name']
				self.products['sku'] = int(sku)

				time.sleep(random.randint(0,1)/4)
				while not self.empty_review:
					time.sleep(random.randint(0,1)/4)
					url_products = f'https://pdp-api.extra.com.br/api/v2/reviews/product/{product["id"]}/source/EX?page={self.page_reviews}'
					yield response.follow(url=url_products, callback=self.parse_reviews)

			time.sleep(random.randint(0,1)/4)
			self.page_products += 1
			url_products = f'http://www.extra.com.br/api/catalogo-ssr/products/?Filtro={self.filters["coolers"]}&PaginaAtual={self.page_products}'
			yield response.follow(url=url_products, callback=self.parse)
			
	def parse_reviews(self, response):
		data = json.loads(response.text)

		if data['review']['userReviews']:
			for review in data['review']['userReviews']:
					self.item_review['id'] = review['id']
					self.item_review['product_id'] = self.products['id']
					self.item_review['product_sku'] = self.products['sku']
					self.item_review['product_name'] = self.products['title']
					self.item_review['text'] = review['text']
					self.item_review['rating'] = review['rating']
					self.item_review['date'] = review['date']
					self.item_review['dislikes'] = review['dislikes']
					self.item_review['likes'] = review['likes']

					yield self.item_review

			self.page_reviews += 1

		else:
			self.empty_review = True
