import mechanicalsoup


def single_pattern(urls_to_follow):
	# this pattern is a single table with 10 to 21 rows
	for web in urls_to_follow: 

		new_browser = mechanicalsoup.Browser() # creating a new browser page
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


def tables_pattern(urls_to_follow):
	# this pattern is a multi table page that has 4 to 12 tables init
	for web in urls_to_follow: 

		new_browser = mechanicalsoup.Browser() # creating a new browser page
		league = new_browser.get(web)

		divisons = league.soup.findAll('div', {'class':'football__group'})
		name = league.soup.find('caption')

		print(f'\n>> {name.text.strip()}')

		for div in divisons: # scraping each table with row init
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