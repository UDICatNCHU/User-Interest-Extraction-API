# Usage

`index.html` provide a web service by loading json  
When you start to look up those data.  
you need to run scrapy command first to get those json file.

`scrapy crawl Attractions -o attractions.json -t json`: This command will download data from Attractions of tripadvisor.
`scrapy crawl restaurant -o restaurant.json -t json`: same as beyond.

`comprehensiveCrawler.py` is a web crawler which can get the information from ESPN, CNET and IMDB, and organize them into JSON files for sports news, tech news and movie inforamtion respectively. The JSON files will be created in ./result/.