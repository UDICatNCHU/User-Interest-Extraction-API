# -*- coding: utf-8 -*-
import scrapy, json, functools
from bs4 import BeautifulSoup
from tripadvisor.items import TripadvisorItem

class YahoomovieSpider(scrapy.Spider):
    name = "yahoomovie"
    allowed_domains = ["tw.movies.yahoo.com"]
    start_urls = ['https://tw.movies.yahoo.com/chart.html']

    def parse(self, response):
        soup = BeautifulSoup(response.body)
        for i in soup.select('div.tr')[1:]:
            yield scrapy.Request(i.select('a')[0]['href'], self.parse_detail)

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