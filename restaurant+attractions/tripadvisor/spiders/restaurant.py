# -*- coding: utf-8 -*-
import scrapy, json, functools
from bs4 import BeautifulSoup
from tripadvisor.items import TripadvisorItem

class RestaurantSpider(scrapy.Spider):
    name = "restaurant"
    allowed_domains = ["www.tripadvisor.com"]
    start_urls = ['https://www.tripadvisor.com/Restaurants-g294265-Singapore.html']

    def parse(self, response):
        res = BeautifulSoup(response.body)
        for i in res.select('.property_title'):
            yield scrapy.Request('http://'+self.allowed_domains[0] + i['href'], self.parse_detail)

    def parse_detail(self, response):
        res = BeautifulSoup(response.body)
        tripItem = TripadvisorItem()
        tripItem['title'] = res.select('#HEADING')[0].text.replace('\n', '')
        tripItem['location'] = res.select('.format_address')[0].text
        tripItem['description'] = functools.reduce(lambda x,y:x+y, map(lambda review:review.text, res.select('.partial_entry'))).replace('\n', '', 1).replace('More\xa0 \n', '')
        tripItem['category'] = "event"
        tripItem['type'] = "restaurant"
        tripItem['channel'] = ""
        tripItem['time'] = ""
        tripItem['price'] = 0
        tripItem['image'] = ""
        tripItem['link'] = response.url
        return tripItem
