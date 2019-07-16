from bs4 import BeautifulSoup
import requests

page = requests.get('http://www.dnk.de/Denkmalschutz/n2277?node_id=2295')
soup = BeautifulSoup(page.content, 'html.parser')

links = soup.find('ul', attrs={'class': 'linkliste'}).find_all('a')
prefix = 'http://www.dnk.de/Denkmalschutz/n2277'
for link in links:
	single_page = requests.get(prefix + link.get('href'))
	single_soup = BeautifulSoup(single_page.content, 'html.parser')

	for i in single_soup.find_all('p'):
		print(i)

	

	
	

