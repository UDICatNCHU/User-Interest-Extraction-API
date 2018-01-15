# -*- coding: utf-8 -*-
import scrapy, json, functools
from bs4 import BeautifulSoup
from tripadvisor.items import TripadvisorItem

class YahoomovieSpider(scrapy.Spider):
    name = "yahoomovie"
    allowed_domains = ["movies.yahoo.com.tw"]
    start_urls = ['https://movies.yahoo.com.tw/chart.html']
    
    def parse(self, response):
        soup = BeautifulSoup(response.body)
        num = 1
        for i in soup.select('div.tr')[1:]:
            try:                                #判斷是否有網址
                yield scrapy.Request(i.select('a')[0]['href'], self.parse_detail)
            except:
                yield scrapy.Request(soup.select('div.tr')[num].select('a')[0]['href'], self.parse_detail)
                num += 1
                print(num)
            
                    
       
    def parse_detail(self, response):       
        res = BeautifulSoup(response.body)
        tripItem = TripadvisorItem()
        tripItem['title'] = res.select('.movie_intro_info_r h1')[0].text.replace('\n', '')
        tripItem['location'] = ""
        tripItem['description'] = res.select('.gray_infobox_inner span')[0].text
        tripItem['category'] = "event"
        tripItem['type'] = "yahoomovie"
        tripItem['channel'] = ""
        tripItem['time'] = [i.text for i in res.select('div span') if '上映日期' in i.text][0].replace('上映日期：','')
        tripItem['price'] = 0
        tripItem['image'] = res.select('.movie_intro_foto img')[0]['src']
        tripItem['link'] = response.url
        return tripItem
