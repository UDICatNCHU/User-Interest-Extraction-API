import subprocess, json, time
while True:
	subprocess.call(['rm', '../user_interest_api_server/yahoomovie.json'])
	subprocess.call(['scrapy' ,'crawl' ,'yahoomovie' ,'-o' ,'../user_interest_api_server/yahoomovie.json' ,'-t' ,'json'])
	data = sorted(json.load(open('../user_interest_api_server/yahoomovie.json','r')), key=lambda x:x['time'], reverse=True)
	json.dump(data, open('../user_interest_api_server/yahoomovie.json','w'))
	time.sleep(10000)