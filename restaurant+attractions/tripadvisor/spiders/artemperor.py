# -*- coding: utf-8 -*-
import scrapy, json, functools
from bs4 import BeautifulSoup
from tripadvisor.items import TripadvisorItem


class ArtemperorSpider(scrapy.Spider):
    name = "artemperor"
    allowed_domains = ["artemperor.tw"]
    start_urls = ['http://artemperor.tw/', 'http://artemperor.tw/news?page=2']

    def parse(self, response):
        soup = BeautifulSoup(response.body)
        for i in soup.select('li.news_block'):
            yield scrapy.Request(i.select('a')[0]['href'], self.parse_detail, meta={'img':i.select('img')[0]['src'], 'title':i.select('img')[0]['alt'], 'time':i.select('i')[0].text})

    def parse_detail(self, response):
        res = BeautifulSoup(response.body)
        tripItem = TripadvisorItem()
        tripItem['title'] = response.meta['title']
        tripItem['location'] = ""
        tripItem['description'] = res.select('.content p')[0].text
        tripItem['category'] = "event"
        tripItem['type'] = "artemperor"
        tripItem['channel'] = ""
        tripItem['time'] = response.meta['time']
        tripItem['price'] = 0
        tripItem['image'] = response.meta['img']
        tripItem['link'] = response.url
        return tripItem