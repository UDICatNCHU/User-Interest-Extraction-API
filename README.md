# API

## parameter:
* event: these are available options
	* `rest`
	* `tourist`
	* `Movies`
	* `TechNews`
	* `SportsNews`
	* `ithome`
	* `taiwan_attractions`
	* `taiwan_restaurant`
	* `yahoosport`
	* `yahoomovie`
	* `politics`
	* `art`
* `num`: please don't query num bigger than `20`, some type of event json didn't prepare for that much.

## API url:
example : `140.120.13.243:12435/api/?event=SportsNews&num=20`


# Usage
`index.html` provide a web service by loading json  
When you start to look up those data.  
you need to run scrapy command first to get those json file.

* scrapy:
	* `scrapy crawl Attractions -o attractions.json -t json` from tripadvisor
	* `scrapy crawl restaurant -o restaurant.json -t json` from tripadvisor
	* `scrapy crawl taiwan_attractions -o taiwan_attractions.json -t json` from taiwan tripadvisor
	* `scrapy crawl taiwan_restaurant -o taiwan_restaurant.json -t json` from taiwan restaurant
	* `scrapy crawl ithome -o ithome.json -t json` from ithome
	* `scrapy crawl yahoomovie -o yahoomovie.json -t json` from movie board of yahoo
		* use `python scrapy_background.py` to activate
	* `scrapy crawl artemperor -o art.json -t json` from movie board of yahoo
		* use `python scrapy_background.py` to activate
	* `scrapy crawl politics -o politics.json -t json` from movie board of yahoo
		* use `python scrapy_background.py` to activate
* seperate crawlers:
	* `comprehensiveCrawler.py` is a web crawler which can get the information from __ESPN__, __CNET__ and __IMDB__, and organize them into JSON files for sports news, tech news and movie inforamtion respectively. The JSON files will be created in __./result/__.
	* `python yahoo_sport.py` from sport board of yahoo
