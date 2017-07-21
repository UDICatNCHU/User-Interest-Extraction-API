import time, subprocess

while True:
	subprocess.call(['rm', '../user_interest_api_server/yahoomovie.json'])
	subprocess.call(['scrapy' ,'crawl' ,'yahoomovie' ,'-o' ,'../user_interest_api_server/yahoomovie.json' ,'-t' ,'json'])

	subprocess.call(['rm', '../user_interest_api_server/art.json'])
	subprocess.call(['scrapy' ,'crawl' ,'artemperor' ,'-o' ,'../user_interest_api_server/art.json' ,'-t' ,'json'])
	time.sleep(3000)