import os
import sys
import shutil

SCRIPT_PARAMS = sys.argv[1:]
HOME = os.getenv("HOME")

BASE_DIRECTORIES = ["Desktop", "Documents", "Downloads", "Music", "Pictures", "Public", "Videos"]

# If the parent folder of this script is visible, hide it.
def hide():
	old_name = os.getcwd() # The path to the directory of containing this code
	BASENAME = os.path.basename( old_name ) # The name of the directory containing this code

	if( not isHiddenFile(BASENAME) ):
		print("Renaming Folder")
		new_base_name = "." + BASENAME
		new_name = os.path.abspath(os.path.join(os.pardir, new_base_name))
		print(old_name, "to", new_name)
		os.rename(old_name, new_name)
	print("now", os.getcwd())
		

def move():
	SCRIPT_LOCATION = os.getcwd() # The path to the directory of containing this code
	#BASENAME = os.path.basename( path_to_dir ) # The name of the directory containing this code
	#print("Move", path_to_dir, BASENAME)
	print("Moving", SCRIPT_LOCATION, "to", HOME)
	shutil.move(SCRIPT_LOCATION, HOME)


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

	# Iterate through contents of Home
	for content in os.listdir():
		# Don't delete hidden files within Home directory and dont delete the base directory
		if( (not isHiddenFile(content)) and (content not in BASE_DIRECTORIES) ): 
			path_of_content = os.path.join(HOME, content)
			print("REMOVING", path_of_content)
			removeContent(path_of_content)

	print("Finished Cleaning")


if __name__ == "__main__":
	FLAG = None

	if(len(SCRIPT_PARAMS) > 0 ):
		FLAG = SCRIPT_PARAMS[0]

		if(FLAG == "hide"):
			hide()
		
		elif(FLAG == "move"):
			move()
	else:
		pass
		#main()
