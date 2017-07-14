# -*- coding: utf-8 -*-
import scrapy, functools
from bs4 import BeautifulSoup
from tripadvisor.items import TripadvisorItem


class TaiwanRestaurantSpider(scrapy.Spider):
    name = "taiwan_restaurant"
    allowed_domains = ["www.tripadvisor.com.tw"]
    start_urls = ['https://www.tripadvisor.com.tw/Tourism-g293913-Taipei-Vacations.html', 'https://www.tripadvisor.com.tw/Tourism-g297910-Taichung-Vacations.html', 'https://www.tripadvisor.com.tw/Tourism-g1432365-Xinbei-Vacations.html', 'https://www.tripadvisor.com.tw/Tourism-g297908-Kaohsiung-Vacations.html', 'https://www.tripadvisor.com.tw/Tourism-g293912-Tainan-Vacations.html', 'https://www.tripadvisor.com.tw/Tourism-g297907-Hualien_County-Vacations.html', 'https://www.tripadvisor.com.tw/Tourism-g297909-Pingtung_County-Vacations.html', 'https://www.tripadvisor.com.tw/Tourism-g304163-Taitung_County-Vacations.html', 'https://www.tripadvisor.com.tw/Tourism-g304160-Nantou_County-Vacations.html']

    def parse(self, response):
        res = BeautifulSoup(response.body)
        for i in res.select('.restaurants li'):
            yield scrapy.Request('http://'+self.allowed_domains[0] + i.select('a')[0]['href'], self.parse_detail)

    def parse_detail(self, response):
        res = BeautifulSoup(response.body)
        tripItem = TripadvisorItem()
        tripItem['title'] = res.select('#HEADING')[0].text.replace('\n', '')
        tripItem['location'] = res.select('.colCnt2')[0].text
        tripItem['description'] = functools.reduce(lambda x,y:x+'\n'+y, map(lambda review:review.text, res.select('.partial_entry'))).replace('\n', '', 1).replace('More\xa0 \n', '')
        tripItem['category'] = "event"
        tripItem['type'] = "restaurant"
        tripItem['channel'] = ""
        tripItem['time'] = ""
        tripItem['price'] = 0
        tripItem['image'] = res.select('.prw_rup.prw_common_centered_image.photo')[-1].select('img')[0]['src']
        tripItem['link'] = response.url
        return tripItem
