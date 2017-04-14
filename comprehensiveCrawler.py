from bs4 import BeautifulSoup
from datetime import datetime
import requests
import xml.etree.ElementTree as ET
import pprint
import collections
import json


class SportsCrawler(object):
    def __init__(self):
        self.url = 'http://www.espn.com/espn/rss/news'


    def getResultDict(self):
        resultDict = dict()
        resultDict['item'] = list()

        res = requests.get(self.url)
        tree_root = ET.fromstring(res.content)
        # print(tree_root[0][9][0].text)
        for item in tree_root[0].findall('item'):
            appendDict = collections.OrderedDict()
            appendDict['title'] = item.find('title').text
            appendDict['category'] = 'news'
            appendDict['type'] = 'sports'
            appendDict['channel'] = 'ESPN'
            appendDict['time'] = item.find('pubDate').text
            appendDict['location'] = 'United States'
            appendDict['price'] = 0
            appendDict['image'] = ''
            
            link = item.find('link').text
            appendDict['description'] = self.getDescriptions(link)
            appendDict['link'] = link
            resultDict['item'].append(appendDict)
        # pprint.pprint(self.resultDict)
        return resultDict


    def getDescriptions(self, link):
        res = requests.get(link)
        soup = BeautifulSoup(res.text, 'html.parser')
        returnStr = ''
        for item in soup.find_all('p')[0:4]:
            returnStr += item.text

        return returnStr


    def dumpToJson(self, resultDict):
        with open('./result/SportsNews.json', 'w') as wf:
            json.dump(resultDict, wf)


    def exec(self):
        print('==================')
        print('正在爬取體育新聞...')
        print('現在時間： ' + str(datetime.now()))
        writeDict = self.getResultDict()
        self.dumpToJson(writeDict)
        print('體育新聞寫檔完成')


class TechNewsCrawler(object):
    def __init__(self):
        self.url = 'https://www.cnet.com/rss/news/'


    def parseXmlToDict(self):
        resultDict = dict()
        resultDict['item'] = list()

        res = requests.get(self.url)
        tree_root = ET.fromstring(res.content)
        for item in tree_root[0].findall('item'):
            # print(item.find('title').text)
            appendDict = collections.OrderedDict()
            appendDict['title'] = item.find('title').text
            appendDict['category'] = 'news'
            appendDict['type'] = 'tech'
            appendDict['channel'] = 'CNET'
            appendDict['time'] = item.find('pubDate').text
            appendDict['location'] = ''
            appendDict['price'] = 0
            appendDict['image'] = ''
            appendDict['description'] = item.find('description').text
            appendDict['link'] = item.find('link').text
            resultDict['item'].append(appendDict)
        # pprint.pprint(self.resultDict)
        return resultDict


    def dumpToJson(self, resultDict):
        with open('./result/TechNews.json', 'w') as wf:
            json.dump(resultDict, wf)


    def exec(self):
        print('==================')
        print('正在爬取科技新聞...')
        print('現在時間： ' + str(datetime.now()))
        writeDict = self.parseXmlToDict()
        self.dumpToJson(writeDict)
        print('科技新聞寫檔完成')







if __name__ == '__main__':
    sportsObj = SportsCrawler()
    sportsObj.exec()

    TechNewsObj = TechNewsCrawler()
    TechNewsObj.exec()