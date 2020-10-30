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

new_browser = mechanicalsoup.Browser()
primer_page = new_browser.get(urls_to_follow[0])
