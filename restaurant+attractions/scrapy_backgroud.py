import time, subprocess, json

while True:
	subprocess.call(['rm', '../user_interest_api_server/yahoomovie.json'])
	subprocess.call(['scrapy' ,'crawl' ,'yahoomovie' ,'-o' ,'../user_interest_api_server/yahoomovie.json' ,'-t' ,'json'])
	with open('../user_interest_api_server/yahoomovie.json', 'r') as f:
		file = json.load(f)
	with open('../user_interest_api_server/yahoomovie.json', 'w') as f:
		json.dump(sorted(file, key=lambda x:x['time'], reverse=True), f) 

	subprocess.call(['rm', '../user_interest_api_server/art.json'])
	subprocess.call(['scrapy' ,'crawl' ,'artemperor' ,'-o' ,'../user_interest_api_server/art.json' ,'-t' ,'json'])
	with open('../user_interest_api_server/art.json', 'r') as f:
		file = json.load(f)
	with open('../user_interest_api_server/art.json', 'w') as f:
		json.dump(sorted([i for i in file if '展期' not in i['time']], key=lambda x:x['time'], reverse=True), f)

	time.sleep(3000)