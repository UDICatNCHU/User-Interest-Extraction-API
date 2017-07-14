# -*- coding: utf-8 -*-
import scrapy, functools
from bs4 import BeautifulSoup
from tripadvisor.items import TripadvisorItem

class IthomeSpider(scrapy.Spider):
	name = "ithome"
	allowed_domains = ["www.ithome.com.tw"]
	start_urls = ['http://www.ithome.com.tw/security', 'http://www.ithome.com.tw/big-data']

	def parse(self, response):
		res = BeautifulSoup(response.body)
		for i in res.select('.item'):
			yield scrapy.Request('http://'+self.allowed_domains[0] + i.select('a')[0]['href'], self.parse_detail)

	def parse_detail(self, response):
		res = BeautifulSoup(response.body)
		tripItem = TripadvisorItem()
		tripItem['title'] = res.select('.page-header')[0].text.replace('\n', '')
		tripItem['location'] = ''
		tripItem['description'] = functools.reduce(lambda x,y:x+'\n'+y, map(lambda review:review.text, res.select('.even p'))).replace('\n', '', 1)
		tripItem['category'] = "event"
		tripItem['type'] = "it"
		tripItem['channel'] = ""
		tripItem['time'] = res.select('#block-views-view-news-custom-submitted .created')[0].text
		tripItem['price'] = 0
		tripItem['image'] = res.select('.img-wrapper img')[0]['src']
		tripItem['link'] = response.url
		return tripItem