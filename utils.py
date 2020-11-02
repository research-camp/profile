import os
import datetime


MAIN_DIR = "./docs/"
FORMAT = ".txt"
DATE_PATTERN = "%B %d %Y - %I:%M %p"


def dir_check(path):
	if not os.path.exists(path):
		os.mkdir(path)


def init_file():
	year_dir = datetime.datetime.now().strftime("%Y") + "/"
	month_dir = datetime.datetime.now().strftime("%m") + "/"
	name = datetime.datetime.now().strftime("%d")
	dir_check(MAIN_DIR)
	dir_check(MAIN_DIR + year_dir)	
	dir_check(MAIN_DIR + year_dir + month_dir)	
	file_path = MAIN_DIR + year_dir + month_dir + name + FORMAT
	with open(file_path, 'w') as file:
		file.write(f'> {datetime.datetime.now().strftime(DATE_PATTERN)}\n\n')


def save_to_now(string):
	year_dir = datetime.datetime.now().strftime("%Y") + "/"
	month_dir = datetime.datetime.now().strftime("%m") + "/"
	name = datetime.datetime.now().strftime("%d")
	file_path =MAIN_DIR + year_dir + month_dir + name + FORMAT
	with open(file_path, 'a+') as file:
		file.write(string)
	