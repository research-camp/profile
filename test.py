import mechanicalsoup

url = 'https://www.theguardian.com/football/tables' # web site we use for data

browser = mechanicalsoup.Browser()

front_page = browser.get(url)
soup_front = front_page.soup

links = soup_front.findAll('a', {'class':'full-table-link'}) # other pages urls

urls_to_follow = [] # we modify the urls in a pattern that works correctly

for link in links:
	new_url = front_page.url[:-16] + link['href'] # create a full domain name
	urls_to_follow.append(new_url)

for web in urls_to_follow[:6]: # the pattern changes after row 6

	new_browser = mechanicalsoup.Browser()
	league = new_browser.get(web)

	rows = league.soup.findAll('tr') # get all the table lines
	name = league.soup.find('caption') # get the league name

	print(f'\n>> {name.text.strip()}')

	for i in range(1,len(rows)): # an iteration over table rows
		print(f'{i}.', end="")
		try:
			link = rows[i].find('a')
			print(link.text.strip(), end="")
		except:
			try:
				team = rows[i].find('span')
				print(team.text.strip(), end="")
			except:
				print('NVFA', end="")
		points = rows[i].find('b')
		print(f" : {points.text.strip()}")

for web in urls_to_follow[6:9]: # this is the middle tables in different pattern
	new_browser = mechanicalsoup.Browser()
	league = new_browser.get(web)

	divisons = league.soup.findAll('div', {'class':'football__group'})
	name = league.soup.find('caption')

	print(f'\n>> {name.text.strip()}')

	for div in divisons: # these pages have a bit different pattern
		print(f'{div.h4.text.strip()}')

		rows = div.findAll('tr')

		for i in range(1,len(rows)):
			print(f'    {i}.', end="")
			try:
				link = rows[i].find('a')
				print(link.text.strip(), end="")
			except:
				try:
					team = rows[i].find('span')
					print(team.text.strip(), end="")
				except:
					print('NVFA', end="")
			points = rows[i].find('b')
			print(f" : {points.text.strip()}")

for web in urls_to_follow[9:-2]: # the normal pattern

	new_browser = mechanicalsoup.Browser()
	league = new_browser.get(web)

	rows = league.soup.findAll('tr')
	name = league.soup.find('caption')

	print(f'\n>> {name.text.strip()}')

	for i in range(1,len(rows)):
		print(f'{i}.', end="")
		try:
			link = rows[i].find('a')
			print(link.text.strip(), end="")
		except:
			try:
				team = rows[i].find('span')
				print(team.text.strip(), end="")
			except:
				print('NVFA', end="")
		points = rows[i].find('b')
		print(f" : {points.text.strip()}")

for web in urls_to_follow[-2:]: # this is the last2 tables in different pattern
	new_browser = mechanicalsoup.Browser()
	league = new_browser.get(web)

	divisons = league.soup.findAll('div', {'class':'football__group'})
	name = league.soup.find('caption')

	print(f'\n>> {name.text.strip()}')

	for div in divisons:
		print(f'{div.h4.text.strip()}')

		rows = div.findAll('tr')

		for i in range(1,len(rows)):
			print(f'    {i}.', end="")
			try:
				link = rows[i].find('a')
				print(link.text.strip(), end="")
			except:
				try:
					team = rows[i].find('span')
					print(team.text.strip(), end="")
				except:
					print('NVFA', end="")
			points = rows[i].find('b')
			print(f" : {points.text.strip()}")