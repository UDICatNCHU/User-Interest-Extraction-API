# -*- coding: utf-8 -*-
import scrapy, functools
from bs4 import BeautifulSoup
from tripadvisor.items import TripadvisorItem
from selenium import webdriver

class TaiwanRestaurantSpider(scrapy.Spider):
    name = "taiwan_attractions"
    allowed_domains = ["www.tripadvisor.com.tw"]
    start_urls = ['https://www.tripadvisor.com.tw/Attractions-g297906-Activities-Hsinchu.html']
    driver = webdriver.PhantomJS(executable_path='./phantomjs')


    def parse(self, response):
        self.driver.get(response.url)
        res = BeautifulSoup(self.driver.page_source)
        for i in res.select('.attraction_element'):
            yield scrapy.Request('http://'+self.allowed_domains[0] + i.select('a')[0]['href'], self.parse_detail)
        self.driver.close()

    def parse_detail(self, response):
        res = BeautifulSoup(response.body)
        tripItem = TripadvisorItem()
        tripItem['title'] = res.select('#HEADING')[0].text.replace('\n', '')
        tripItem['location'] = res.select('.colCnt2')[0].text if len(res.select('.colCnt2')) else ''
        tripItem['description'] = functools.reduce(lambda x,y:x+'\n'+y, map(lambda review:review.text, res.select('.partial_entry'))).replace('\n', '', 1).replace('More\xa0 \n', '')
        tripItem['category'] = "event"
        tripItem['type'] = "attrations"
        tripItem['channel'] = ""
        tripItem['time'] = ""
        tripItem['price'] = 0
        tripItem['image'] = res.select('.prw_rup.prw_common_centered_image.photo')[-1].select('img')[0]['src']
        tripItem['link'] = response.url
        return tripItem
