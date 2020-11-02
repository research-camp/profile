import mechanicalsoup

from scrape import single_pattern, tables_pattern

url = 'https://www.theguardian.com/football/tables' # web site we use for data

browser = mechanicalsoup.Browser()

front_page = browser.get(url)
soup_front = front_page.soup

links = soup_front.findAll('a', {'class':'full-table-link'}) # other pages urls

urls_to_follow = [] # we modify the urls in a pattern that works correctly

for link in links:
	new_url = front_page.url[:-16] + link['href'] # create a full domain name
	urls_to_follow.append(new_url)

single_pattern(urls_to_follow[:6]) # the pattern changes after row 6
	

tables_pattern(urls_to_follow[6:9]) # this is the middle tables in different pattern
	

single_pattern(urls_to_follow[9:-2]) # the normal pattern


tables_pattern(urls_to_follow[-2:]) # this is the last2 tables in different pattern