# -*- coding: utf-8 -*-
import scrapy, json, functools
from bs4 import BeautifulSoup
from tripadvisor.items import TripadvisorItem

class AttractionsSpider(scrapy.Spider):
    name = "Attractions"
    allowed_domains = ["www.tripadvisor.com"]
    start_urls = ['https://www.tripadvisor.com/Attractions-g294265-Activities-c57-Singapore.html/']

    def parse(self, response):
        res = BeautifulSoup(response.body)
        for i in res.select('div.photo_booking.non_generic a'):
            yield scrapy.Request('http://'+self.allowed_domains[0] + i['href'], self.parse_detail)

    def parse_detail(self, response):
        res = BeautifulSoup(response.body)
        tripItem = TripadvisorItem()
        tripItem['title'] = res.select('#HEADING')[0].text
        tripItem['location'] = res.select('.format_address')[0].text
        tripItem['description'] = functools.reduce(lambda x,y:x+y, map(lambda review:review.text, res.select('.partial_entry')))
        tripItem['category'] = "event"
        tripItem['type'] = "attractions"
        tripItem['channel'] = ""
        tripItem['time'] = ""
        tripItem['price'] = ""
        tripItem['image'] = ""
        tripItem['link'] = response.url
        return tripItem