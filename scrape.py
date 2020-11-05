import mechanicalsoup

from utils import save_to_now, save_to_html, write_in_html


def single_pattern(urls_to_follow):
	# this pattern is a single table with 10 to 21 rows
	final_string = ""
	for web in urls_to_follow: 

		final_dic = {}

		new_browser = mechanicalsoup.Browser() # creating a new browser page
		league = new_browser.get(web)

		rows = league.soup.findAll('tr') # get all the table lines
		name = league.soup.find('caption') # get the league name

		final_string += f'\n>> {name.text.strip()}\n'

		for i in range(1,len(rows)): # an iteration over table rows
			final_string += f'{i}.'
			final_dic[str(i)] = []
			cols = rows[i].findAll('td')
			try:
				link = rows[i].find('a')
				final_string += link.text.strip()
				final_dic[str(i)].append(link.text.strip())
			except:
				try:
					team = rows[i].find('span')
					final_string += team.text.strip()
					final_dic[str(i)].append(team.text.strip())
				except:
					final_string += 'NVFA'
					final_dic[str(i)].append('NVFA')
			points = rows[i].find('b')
			final_string += f" GP: {cols[2].text.strip()}"
			final_string += f" Pts: {points.text.strip()}\n"
			final_dic[str(i)].append(cols[2].text.strip())
			final_dic[str(i)].append(points.text.strip())

		save_to_html(name.text.strip(), final_dic)

	save_to_now(final_string) # saving the whole thing inside a text file


def tables_pattern(urls_to_follow):
	# this pattern is a multi table page that has 4 to 12 tables init
	final_string = ""
	for web in urls_to_follow: 

		new_browser = mechanicalsoup.Browser() # creating a new browser page
		league = new_browser.get(web)

		divisons = league.soup.findAll('div', {'class':'football__group'})
		name = league.soup.find('caption')

		final_string += f'\n>> {name.text.strip()}\n'
		write_in_html(f'<h3>{name.text.strip()}</h3>')

		for div in divisons: # scraping each table with row init
			final_string += f'{div.h4.text.strip()}\n'
			
			final_dic = {}

			rows = div.findAll('tr')

			for i in range(1,len(rows)):
				final_string += f'    {i}.'
				final_dic[str(i)] = []
				cols = rows[i].findAll('td')
				try:
					link = rows[i].find('a')
					final_string += link.text.strip()
					final_dic[str(i)].append(link.text.strip())
				except:
					try:
						team = rows[i].find('span')
						final_string += team.text.strip()
						final_dic[str(i)].append(team.text.strip())
					except:
						final_string += 'NVFA'
						final_dic[str(i)].append('NVFA')
				points = rows[i].find('b')
				final_string += f" GP: {cols[2].text.strip()}"
				final_string += f" Pts: {points.text.strip()}\n"
				final_dic[str(i)].append(cols[2].text.strip())
				final_dic[str(i)].append(points.text.strip())

			save_to_html(div.h4.text.strip(), final_dic)

	save_to_now(final_string) # saving the whole thing inside a text file	