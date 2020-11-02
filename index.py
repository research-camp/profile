import mechanicalsoup

from scrape import single_pattern, tables_pattern
from utils import init_filem, save_to_now


url = 'https://www.theguardian.com/football/tables' # web site we use for data
DOMAIN_NAME = 'https://www.theguardian.com/'


def init():
	global url

	init_file() # creating the output files

	browser = mechanicalsoup.Browser() # creating a new browser

	try:
		front_page = browser.get(url) # getting the first page
	except (e,): # hadeling the connection or any errors
		save_to_now(str(e))

	soup_front = front_page.soup

	links = soup_front.findAll('a', {'class':'full-table-link'}) 
	# we are getting other pages urls from href a tags so first we collect them

	urls_to_follow = [] # we modify the urls in a pattern that works correctly

	for link in links:
		# create a full domain name from a tags in the website
		new_url = DOMAIN_NAME + link['href'] 
		urls_to_follow.append(new_url)

	single_pattern(urls_to_follow[:6]) 
	# the pattern changes after row 6
	tables_pattern(urls_to_follow[6:9]) 
	# this is the middle tables in different pattern
	single_pattern(urls_to_follow[9:-2]) 
	# the normal pattern
	tables_pattern(urls_to_follow[-2:]) 
	# this is the last2 tables in different pattern


if __name__ == "__main__":
	init()