import requests, json
from bs4 import BeautifulSoup


def main():
	jsonArray = []
	yahooMovies_url = 'https://tw.movies.yahoo.com/chart.html/'
	res = requests.get(yahooMovies_url)
	soup = BeautifulSoup(res.text,'html.parser')
	array = soup.select('div[class="tr"]')
	
	for movie in array:
		title = ""
		if movie.div.text == '1':
			title = movie.h1.string
		else:
			rank_txt = movie.select('.rank_txt')
			title = rank_txt[0].string

		link = movie.a.get('href')
		res_movie = requests.get(link)
		soup_movie = BeautifulSoup(res_movie.text,'html.parser')
		image = soup_movie.select('div[class="movie_intro_foto"]')[0].img['src']
		description = soup_movie.select('.gray_infobox_inner span')[0].text
		time = soup_movie.select('.movie_intro_info_r span')[0].text

		result = {'description':description, 'price':"", 'link':link, 'category':'event', 
						'type':'movie', 'channel':"", 'title':title, 'location':"", 'time':time[-10:], 'image':image}
		jsonArray.append(result)
		
	json.dump(jsonArray,open('yahooMovies.json','w'))



if __name__ == "__main__":
	main()