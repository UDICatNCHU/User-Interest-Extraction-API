# -*- coding: utf-8 -*-
import scrapy, json, functools
from bs4 import BeautifulSoup
from tripadvisor.items import TripadvisorItem


class ArtemperorSpider(scrapy.Spider):
    name = "artemperor"
    allowed_domains = ["artemperor.tw"]
    start_urls = ['http://artemperor.tw/tidbits'] + ['http://artemperor.tw/tidbits?page={}'.format(str(i)) for i in range(422)]

    def parse(self, response):
        soup = BeautifulSoup(response.body)
        for i in soup.select('li.exhibit_block'):
            if '新竹' in i.text:
                yield scrapy.Request(i.select('a')[0]['href'], self.parse_detail, meta={'img':i.select('img')[0]['src'], 'title':i.select('img')[0]['alt'], 'time':[i.text for i in i.select('p') if '日期' in i.text][0]})

    def parse_detail(self, response):
        res = BeautifulSoup(response.body)
        tripItem = TripadvisorItem()
        tripItem['title'] = response.meta['title']
        tripItem['location'] = [i.text for i in res.select('li') if '地點' in i.text][0]
        tripItem['description'] = res.select('.content p')[0].text
        tripItem['category'] = "event"
        tripItem['type'] = "artemperor"
        tripItem['channel'] = ""
        tripItem['time'] = response.meta['time']
        tripItem['price'] = 0
        tripItem['image'] = response.meta['img']
        tripItem['link'] = response.url
        return tripItem