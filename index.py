import os
import sys
import shutil

HOME = os.getenv("HOME")
SCRIPT_LOCATION = os.getcwd()
BASE_DIRECTORIES = ["Desktop", "Documents", "Downloads", "Music", "Pictures", "Public", "Videos"]

def isFolderVisible():
	'''
	Checks if the parent folder of this script is visible
	'''
	BASENAME = os.path.basename(os.getcwd())
	return not isHiddenFile(BASENAME)

def hide():
	'''
	If the parent folder of this script is visible, hide it.
	'''
	old_name = os.getcwd() # The path to the directory of containing this code
	BASENAME = os.path.basename( old_name ) # The name of the directory containing this code

	if( not isHiddenFile(BASENAME) ):
		print("Renaming Folder")
		new_base_name = "." + BASENAME
		new_name = os.path.abspath(os.path.join(os.pardir, new_base_name))
		print(old_name, "to", new_name)
		os.rename(old_name, new_name)

	print("The folder is now called", os.getcwd())
		

def isHiddenFile(filename):
	return filename.startswith('.')

def removeContent(path_of_content):
	'''
	Calls the appropriate commands to remove a file, whether it is a directory or a file
	'''
	if( os.path.isfile( path_of_content ) ): # if content is a file
		os.remove(path_of_content)

	elif( os.path.isdir( path_of_content ) ): # if content is a dir
		shutil.rmtree(path_of_content) # Delete the entire folder, including contents

	else:
		print("Will now remove", path_of_content)

def removeBaseDirectoryFiles():
	'''
	Removes all subdirectories and/or files within each Base Directory
	'''
	os.chdir(HOME)

	# First, remove all files inside each of the base directories, not including Home
	for directory in BASE_DIRECTORIES:
		path_of_base_dir = os.path.join(HOME, directory)
		os.chdir(path_of_base_dir) 

		for content in os.listdir():
			path_of_content = os.path.join(os.getcwd(), content)
			removeContent(path_of_content)
	
def removeHomeFiles():
	'''
	Removes all files within the Home Directory, not including the any of the Base Directories
	'''
	os.chdir(HOME)

	# Iterate through contents of Home
	for content in os.listdir():
		# Don't delete hidden files within Home directory and dont delete the base directory
		if( (not isHiddenFile(content)) and (content not in BASE_DIRECTORIES) ): 
			path_of_content = os.path.join(HOME, content)
			print("REMOVING", path_of_content)
			removeContent(path_of_content)

def removeOldScript():
	old_alias_file = os.path.join(HOME, '.bash_aliases')
	old_directory = os.path.join(HOME, '.127pythonscript')

	if( os.path.isfile( old_alias_file ) ):
		print("Removing old alias file")
		removeContent( old_alias_file )
	if( os.path.isdir( old_directory ) ):
		print("Removing old script directory")
		removeContent( old_directory )
	

def updateScript():
	old_loc = os.getcwd()
	os.chdir(SCRIPT_LOCATION)
	print("Checking for updates from GitHub")
	os.system('git pull origin master')
	os.chdir(old_loc)

def main():
	removeBaseDirectoryFiles()
	removeHomeFiles()
	print("Finished Cleaning")

	# Removes the old version of the script
	removeOldScript()
	# Check for updates at the end of every execution
	updateScript()


if __name__ == "__main__":
	if( isFolderVisible() ):
		hide()
	main()


