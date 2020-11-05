import os
import datetime

from prettytable import PrettyTable


MAIN_DIR = "./docs/"
FORMAT = ".txt"
TABLE_FORMAT = ".html"
DATE_PATTERN = "%B %d %Y - %I:%M %p"


def dir_check(path):
	if not os.path.exists(path):
		os.mkdir(path)


def init_file():
	year_dir = datetime.datetime.now().strftime("%Y") + "/"
	month_dir = datetime.datetime.now().strftime("%m") + "/"
	name = datetime.datetime.now().strftime("%d") + "/"
	dir_check(MAIN_DIR)
	dir_check(MAIN_DIR + year_dir)	
	dir_check(MAIN_DIR + year_dir + month_dir)
	dir_check(MAIN_DIR + year_dir + month_dir + name)	
	file_path = MAIN_DIR + year_dir + month_dir + name + "doc" + FORMAT
	html_path = MAIN_DIR + year_dir + month_dir + name + "table" + TABLE_FORMAT
	with open(file_path, 'w') as file:
		file.write(f'> {datetime.datetime.now().strftime(DATE_PATTERN)}\n\n')
	with open(html_path, 'w') as file:
		file.write(f'<h2>{datetime.datetime.now().strftime(DATE_PATTERN)}</h2>')


def save_to_now(string):
	year_dir = datetime.datetime.now().strftime("%Y") + "/"
	month_dir = datetime.datetime.now().strftime("%m") + "/"
	name = datetime.datetime.now().strftime("%d") + "/"
	file_path = MAIN_DIR + year_dir + month_dir + name + "doc" + FORMAT
	with open(file_path, 'a+') as file:
		file.write(string)


def save_to_html(title, dictionary):
	year_dir = datetime.datetime.now().strftime("%Y") + "/"
	month_dir = datetime.datetime.now().strftime("%m") + "/"
	name = datetime.datetime.now().strftime("%d") + "/"
	file_path = MAIN_DIR + year_dir + month_dir + name + "table" + TABLE_FORMAT

	x = PrettyTable(["Rank", "Team name", "Game play", "Win", 
					 "Draw", "Lose", "Points"])

	for index in dictionary.keys():
		dictionary[index].insert(0, index)
		x.add_row(dictionary[index])

	with open(file_path,'a+') as file:
		file.write(x.get_html_string(title=title))


def write_in_html(string):	
	year_dir = datetime.datetime.now().strftime("%Y") + "/"
	month_dir = datetime.datetime.now().strftime("%m") + "/"
	name = datetime.datetime.now().strftime("%d") + "/"
	file_path = MAIN_DIR + year_dir + month_dir + name + "table" + TABLE_FORMAT

	with open(file_path,'a+') as file:
		file.write(string)
