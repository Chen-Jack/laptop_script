import os
import sys
import shutil

SCRIPT_PARAMS = sys.argv[1:]

SCRIPT_LOCATION = os.getcwd()
HOME = os.getenv("HOME")

BASE_DIRECTORIES = ["Desktop", "Documents", "Downloads", "Music", "Pictures", "Public", "Videos"]


# First, remove all files inside each of the base directories, not including Home
for directory in BASE_DIRECTORIES:
	print("Entering", directory)
	x = os.path.join(HOME, directory)
	os.chdir(x) # Changing directory
	for content in os.listdir():
		path_of_content = os.path.join(os.getcwd(), content)

		if( os.path.isfile( path_of_content ) ): # if content is a file
			print(content, "IS FILE")
			os.remove(path_of_content)

		elif( os.path.isdir( path_of_content ) ): # if content is a dir
			print(content, "IS DIR")
			# shutil.rmtree(path_of_content) # Delete the entire folder, including contents

		else:
			print(content, "NOT FILE")


# Removing all files within Home
os.chdir(HOME)
print("CURRENTLY IN", os.cwd()

	
