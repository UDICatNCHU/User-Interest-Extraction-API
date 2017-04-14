# -*- coding: utf-8 -*-
import scrapy, json
from bs4 import BeautifulSoup
from tripadvisor.items import TripadvisorItem

class RestaurantSpider(scrapy.Spider):
    name = "restaurant"
    allowed_domains = ["www.tripadvisor.com.tw"]
    start_urls = ['https://www.tripadvisor.com/Restaurants-g294265-Singapore.html']

    def parse(self, response):
        res = BeautifulSoup(response.body)
        for i in res.select('.property_title'):
            yield scrapy.Request('http://'+self.allowed_domains[0] + i['href'], self.parse_detail)

    def parse_detail(self, response):
        res = BeautifulSoup(response.body)
        tripItem = TripadvisorItem()
        tripItem['location'] = res.select('#HEADING')[0].text
        tripItem['address'] = res.select('.format_address')[0].text
        tripItem['reviews'] = json.dumps(list(map(lambda review:review.text, res.select('.partial_entry'))))
        return tripItem
