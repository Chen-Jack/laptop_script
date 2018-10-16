import os
import sys
import shuntil

SCRIPT_PARAMS = sys.argv[1:]

SCRIPT_LOCATION = os.getcwd()
HOME = os.getenv("HOME")

BASE_DIRECTORIES = ["Desktop", "Documents", "Downloads", "Music", "Pictures", "Public", "Videos"]



for directory in BASE_DIRECTORIES:
	print("Entering", directory)
	x = os.path.join(HOME, directory)
	os.chdir(x)
	print(os.listdir())
