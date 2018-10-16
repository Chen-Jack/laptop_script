import os
import sys
import shutil

SCRIPT_PARAMS = sys.argv[1:]

SCRIPT_LOCATION = os.getcwd()
HOME = os.getenv("HOME")

BASE_DIRECTORIES = ["Desktop", "Documents", "Downloads", "Music", "Pictures", "Public", "Videos"]


def isHiddenFile(filename):
	return filename.startswith('.')

def removeContent(path_of_content):
	if( os.path.isfile( path_of_content ) ): # if content is a file
		os.remove(path_of_content)

	elif( os.path.isdir( path_of_content ) ): # if content is a dir
		shutil.rmtree(path_of_content) # Delete the entire folder, including contents

	else:
		print("Will not remove", path_of_content)

def main():
	print("Phase 1")
	# First, remove all files inside each of the base directories, not including Home
	for directory in BASE_DIRECTORIES:
		path_of_base_dir = os.path.join(HOME, directory)
		os.chdir(path_of_base_dir) 

		for content in os.listdir():
			path_of_content = os.path.join(os.getcwd(), content)
			removeContent(path_of_content)


	# Removing all files within Home
	print("Phase 2")
	os.chdir(HOME)
	for content in os.listdir(): # Iterate through contents of Home

		# Don't delete hidden files within Home directory and dont delete the base directory
		if( (not isHiddenFile(content)) and (content not in BASE_DIRECTORIES) ): 
			path_of_content = os.path.join(HOME, content)
			print("REMOVING", path_of_content)
			removeContent(path_of_content)

	print("Finished Cleaning")


if __name__ == "__main__":
	main()
