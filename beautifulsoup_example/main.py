import requests
import pandas as pd
from bs4 import BeautifulSoup

def imdb_request():
	""" 
	Makes a request to imdb.com/calendar
	
	Returns:
		string -- The content of the IMDB calendar page
		None -- If the requests was not successful
	"""
	URL = "https://www.imdb.com/calendar/?region=US"
	headers = {
		'User-Agent':'Script'                #who is making the request {e.g. browser,web app,..}
	}
	response = requests.get(URL,headers = headers)
	if response.status_code == 200:
		return response.text
	return None
	
def save_imdb_content(content):
	try:
		with open("imdb.html","w") as file:
			file.write(content)
	except:
		pass
		
def get_imdb_file():
	content = None 
	try:
		with open("imdb.html","r") as file:
			content = file.read()
	except:
		pass
	return content 
	
def get_imdb_content():
	content = get_imdb_file()
	if content:
		return content
	content = imdb_request()
	save_imdb_content(content)
	return content


def create_movie(date_tag,movie_tag):
	movie = {}
	div_data = movie_tag.find('div',{
		'class':'ipc-metadata-list-summary-item__tc'
	})
	title_tag = div_data.a #by nodes (if there is only one 'a')
	
	categories_tag = div_data.find('ul',{
		'class':'ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--no-wrap ipc-inline-list--inline ipc-metadata-list-summary-item__tl base',
		'role':'presentation'
	})
	categories = [li_tag.span.text for li_tag in categories_tag.find_all('li')]
	
	cast_tag = div_data.find('ul',{
		'class':'ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--no-wrap ipc-inline-list--inline ipc-metadata-list-summary-item__stl base',
		'role':'presentation'
	})
	cast = [li_tag.span.text for li_tag in cast_tag.find_all('li')] if cast_tag else []
	
	#movie data
	movie['Date'] = date_tag.text
	movie['Title'] = title_tag.text
	movie['Categories'] = "#".join(categories)
	movie['Cast'] = "#".join(cast)
	return movie
	
def get_movies_data(soup):
	data = []
	articles_tag = soup.find_all('article',{
		'class': 'sc-48add019-1 eovPBi',
		'data-testid': 'calendar-section'
	}) #by label (it returns all)
	
	for article in articles_tag:
		date_tag = article.find('h3') #by label (it returns the first one)
		movies = article.find_all('li',{ 
			'class':'ipc-metadata-list-summary-item ipc-metadata-list-summary-item--click sc-8c2b7f1f-0 bpqYIE',
			'data-testid':'coming-soon-entry'
		})
		for movie_tag in movies:
			movie = create_movie(date_tag,movie_tag)
			data.append(movie)
	df = pd.DataFrame(data)
	return df
	
def main():
	content = get_imdb_content() 
	soup = BeautifulSoup(content,'html.parser')
	df = get_movies_data(soup)
	df.to_csv("imdb.csv")	
		 
if __name__ == '__main__':
	main()
