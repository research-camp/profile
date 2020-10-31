import mechanicalsoup

url = 'https://www.theguardian.com/football/tables'

browser = mechanicalsoup.Browser()

front_page = browser.get(url)
soup_front = front_page.soup

links = soup_front.findAll('a', {'class':'full-table-link'})

urls_to_follow = []

for link in links:
	new_url = front_page.url[:-16] + link['href']
	urls_to_follow.append(new_url)

for web in urls_to_follow:	

	new_browser = mechanicalsoup.Browser()
	league = new_browser.get(web)

	rows = league.soup.findAll('tr')
	name = league.soup.find('a', {'class':'football-matches_heading'})

	print(f'>> {name.text}')

	for i in range(1,len(rows)):
		link = rows[i].find('a')
		try:
			print(strip(link.text))
		except:
			try:
				team = rows[i].find('span')
				print(strip(team.text))
			except:
				print('NVFA')
