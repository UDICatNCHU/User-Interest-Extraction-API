# API

## parameter:
* event: these are available options
	* `rest`
	* `tourist`
	* `Movies`
	* `TechNews`
	* `SportsNews`
* num: please don't query num bigger than `20`, some type of event json didn't prepare for that much.

## API url:

url : `140.120.13.243:12435/api`

example : `140.120.13.243:12435/api/?event=SportsNews&num=20`


# Usage

`comprehensiveCrawler.py` is a web crawler which can get the information from __ESPN__, __CNET__ and __IMDB__, and organize them into JSON files for sports news, tech news and movie inforamtion respectively. The JSON files will be created in __./result/__.

`index.html` provide a web service by loading json  
When you start to look up those data.  
you need to run scrapy command first to get those json file.

`scrapy crawl Attractions -o attractions.json -t json`: This command will download data from Attractions of tripadvisor.
`scrapy crawl restaurant -o restaurant.json -t json`: same as beyond.
