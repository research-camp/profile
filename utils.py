import os
import datetime


MAIN_DIR = "./docs/"
FORMAT = ".txt"
DATE_PATTERN = "%B %d %Y - %I:%M %p"


def dir_check(path):
	if not os.path().exists(path):
		os.mkdir(path)


def init_file():
	year_dir = "./" + datetime.datetime.now().strftime("%Y") + "/"
	month_dir = datetime.datetime.now().strftime("%m") + "/"
	name = datetime.datetime.now().strftime("%d")
	dir_check(year_dir)	
	dir_check(year_dir + month_dir)	
	file_path = year_dir + month_dir + name + FORMAT
	with open(file_path, 'w') as file:
		file.write(datetime.datetime.now().strftime(DATE_PATTERN))


def save_to_now(string):
	