# -*- coding: utf-8 -*-
import scrapy, json, functools
from bs4 import BeautifulSoup
from tripadvisor.items import TripadvisorItem

class PoliticsSpider(scrapy.Spider):
    name = "politics"
    start_urls = ['http://news.ltn.com.tw/list/breakingnews/politics']

    def parse(self, response):
        soup = BeautifulSoup(response.body)  
        jsonArray = []
        for news in soup.select('.imm li a.tit'):
            yield scrapy.Request(news['href'], self.parse_detail)
           
    def parse_detail(self, response):
        res = BeautifulSoup(response.body)
        tripItem = TripadvisorItem()
        title = res.select('h1')[0].text.replace('\n', '')
        tripItem['title'] = title.replace('\t', '')
        tripItem['location'] = ""
        description = ""
        for text in res.select('.text p'):
            if not(text.find_previous_sibling().select('img')):
                description = description + text.text

        tripItem['description'] = description
        tripItem['category'] = "event"
        tripItem['type'] = "politics"
        tripItem['channel'] = ""
        tripItem['time'] = res.select('.text.text span')[0].text
        tripItem['price'] = 0
        if res.select('img.boxInput'):
            try:
                image = res.select('img.boxInput')[0]['src']
            except Exception as e:
                print('==============')
                print(res.select('img.boxInput'))
                print('==============')
        else:
            image = res.select('.pic750 img')[0]['src']
        tripItem['image'] = image
        tripItem['link'] = response.url
        
        return tripItem