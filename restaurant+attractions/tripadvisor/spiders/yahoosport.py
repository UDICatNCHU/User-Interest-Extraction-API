# -*- coding: utf-8 -*-
import scrapy, json, functools
from bs4 import BeautifulSoup
from tripadvisor.items import TripadvisorItem

class YahoosportSpider(scrapy.Spider):
    name = "yahoosport"
    allowed_domains = ["tw.sports.yahoo.com"]
    start_urls = ['https://tw.sports.yahoo.com/site/api/resource/content;getDetailView=true;getFullLcp=false;relatedContent=%7B%22enabled%22%3Atrue%7D;site=sports;useSlingstoneLcp=true;uuids=%5B%22SS-2441cbb0-20ea-3f26-bdfc-d1963ffd3a5d%22%2C%22SS-2769e3b7-6307-3c23-b2ca-0554cb767034%22%2C%22SS-e7c66435-9191-351e-8a3d-bd8b7c90debf%22%2C%22SS-c0f916a6-683a-38a6-b24b-8e28d543527e%22%2C%22SS-8ab404f9-fc2c-3acf-bac8-d286ef9388c1%22%2C%22SS-22babcf6-e13d-35bd-a45a-f16d4b94c037%22%2C%22SS-17deed87-4f61-3be5-97cd-d2c9a701c117%22%2C%22SS-228fde0d-771d-3f86-aede-9291f9a859d8%22%2C%22SS-d6874e41-48c9-333d-873d-c6566784f95a%22%2C%22SS-5ae7c401-961d-3a3c-8986-fb5feaf79b51%22%2C%22SS-d33b3ee3-4b05-36e8-b443-201d7583356d%22%5D?bkt=sports-TW-zh-Hant-TW-def&device=desktop&feature=canvassOffnet&intl=tw&lang=zh-Hant-TW&partner=none&prid=aabeu1tcmu563&region=TW&site=sports&tz=Asia%2FTaipei&ver=1.0.1773&returnMeta=true', 'https://tw.sports.yahoo.com/site/api/resource/content;getDetailView=true;getFullLcp=false;relatedContent=%7B%22enabled%22%3Atrue%7D;site=sports;useSlingstoneLcp=true;uuids=%5B%22d74af5b9-0b77-372d-948a-0def164fc226%22%2C%22f0eabfa3-0645-3a84-91d9-b43a2beeef8e%22%2C%228b9eacdb-cd54-3e30-aea6-6cbbf8ad61fc%22%2C%22SS-e0868a4b-c5a9-3934-b129-5882688bd322%22%2C%22SS-2dfc4a59-35d3-39b2-af65-1c989fbd9693%22%2C%2214a57a55-2fd7-3d5a-bde6-c9519cc1dba5%22%2C%220d7a9efd-f842-363a-8ed6-5fc153004e8c%22%2C%22849d4953-886c-324a-842e-88677ab6ebbc%22%2C%22151da87d-60dd-3ec4-b1d2-3ef73f754356%22%2C%2202d11518-c389-3aa2-8619-4146e6ec576c%22%2C%22b026aa02-ac69-36bb-ac7f-c55ec8acd91a%22%2C%227abb10d5-650a-3aab-b476-2ff84cb8aaf5%22%2C%2228cbc301-831a-32ed-9e36-17732eb71b73%22%2C%22b8851d98-21a1-3329-98b6-af4668398be7%22%5D?bkt=sports-TW-zh-Hant-TW-def&device=desktop&feature=canvassOffnet&intl=tw&lang=zh-Hant-TW&partner=none&prid=265jj3pcmu9gn&region=TW&site=sports&tz=Asia%2FTaipei&ver=1.0.1773&returnMeta=true']

    def parse(self, response):
    	apiData = json.loads(response.text)
    	for i in apiData['data']['items']:
    		yield self.parse_detail(i)

    def parse_detail(self, data):
        tripItem = TripadvisorItem()
        tripItem['title'] = data['title']
        tripItem['location'] = ""
        tripItem['description'] = ''.join([i.get('content', '') for i in data['body'][:-2]])
        tripItem['category'] = "event"
        tripItem['type'] = "yahoosport"
        tripItem['channel'] = ""
        tripItem['time'] = data['publishDateStr']
        tripItem['price'] = 0
        tripItem['image'] = "" if data.get('cover', None) == None else data['cover']['size']['original']['url']
        tripItem['link'] = data['url']
        return tripItem
