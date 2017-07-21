# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
import time 

def main(): 
	driver = webdriver.PhantomJS(executable_path='./phantomjs') # PhantomJs
	time.sleep(1)
	driver.get('https://tw.sports.yahoo.com/')  
	
	
	for i in range(5):  #向下滾動五次
		driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')  # 重複往下捲動
		time.sleep(1)  

	pageSource = driver.page_source  # 取得網頁原始碼
	driver.close()

	soup = BeautifulSoup(pageSource,'lxml')
	data = soup.select('.Cf')
	jsonArray = []
	for x in range(len(data)):
		if data[x].select('.Mb(5px)') and data[x].select('img') and not(data[x].select('.VideoPlayer')):
			link = data[x].select('.Mb(5px)')[0].a.get('href')
			title = data[x].select('.Mb(5px)')[0].a.text
			image = data[x].select('img')[0].get('src')
		
			res = requests.get(link)
			res.encoding = 'utf-8'
			soupData = BeautifulSoup(res.text,'lxml') 
			if soupData.select('.date'):
				datetime = soupData.select('.date')[0].get('datetime')
			else:
				continue

			description = ""
			for ele in soupData.select('.canvas-atom'):
				if ele.get('type') == 'text':
					description = description + ele.text

			#if soupData.select('noscript'):
			#	image = soupData.select('noscript img')[0].get('src')
			#else:
			#	continue
			
			result = {'description' : description, 'price' : "",
					'link' : link, 'category' : "event", 'type' : "sports",
					'channel' : "", 'title' : title, 'location' : "",
					'time' : datetime, 'image' : image}
			jsonArray.append(result)
			if len(jsonArray) >= 20:
				break
		else:
			continue

	json.dump(jsonArray, open('yahoosports.json', 'w'))

if __name__ == '__main__':
	main()
