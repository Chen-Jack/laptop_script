# This script was created by Jack Chen of Hunter College. 
import os
import sys
import shutil
import time

HOME = os.getenv("HOME") 
SCRIPT_LOCATION = os.path.dirname(os.path.realpath(sys.argv[0]))
BASE_DIRECTORIES = ["Desktop", "Documents", "Downloads", "Music", "Pictures", "Public", "Videos"]

def isFolderVisible():
	'''
	Checks if the parent folder of this script is visible
	'''
	BASENAME = os.path.basename(SCRIPT_LOCATION)
	return not isHiddenFile(BASENAME)

def hide():
	'''
	Hides the parent folder of this script and its contents. This is done by 
	simply adding a "." to the basename of the parent folder and renaming it.
	'''
	old_name = SCRIPT_LOCATION # The path to the directory  containing this code
	BASENAME = os.path.basename( old_name ) # The name of the directory containing this code

	if( not isHiddenFile(BASENAME) ): # Only rename if it's not hidden
		print("Renaming Folder")
		new_base_name = "." + BASENAME
		new_name = os.path.abspath(os.path.join(os.pardir, new_base_name))
		print(old_name, "to", new_name)
		os.rename(old_name, new_name)

		

def isHiddenFile(filename):
	'''
	Checks if the file is a hidden file. Note that this only properly
	checks basenames, not a full path. 
	'''
	return filename.startswith('.')

def removeContent(path_of_content, deleteHidden = False):
	'''
	Deletes a file, given a path. Calls the appropriate os functions to do so.
	By default, it will not delete hidden files.
	'''
	if( isHiddenFile(os.path.basename(path_of_content)) and not deleteHidden):
		return
	else:
		print("Attempting to remove", path_of_content)
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

	for directory in BASE_DIRECTORIES:
		path_of_base_dir = os.path.join(HOME, directory)

		for content in os.listdir( path_of_base_dir ):
			path_of_content = os.path.join(path_of_base_dir, content)
			removeContent(path_of_content)
	
def removeHomeFiles():
	'''
	Removes all files within the Home Directory, but not including
	any of the Base Directories
	'''
	os.chdir(HOME)

	# Iterate through contents of Home
	for content in os.listdir():
		# Don't delete hidden files within Home directory 
		# and dont delete the base directory
		if( (not isHiddenFile(content)) and (content not in BASE_DIRECTORIES) ): 
			path_of_content = os.path.join(HOME, content)
			print("REMOVING", path_of_content)
			removeContent(path_of_content)

def removeOldScript():
	'''
	A function to remove the previous iteration of this script.
	Will eventally update main() to no longer need to call this.
	'''
	old_alias_file = os.path.join(HOME, '.bash_aliases')
	old_directory = os.path.join(HOME, '.127pythonscript')

	if( os.path.isfile( old_alias_file ) ):
		print("Removing old alias file")
		os.remove( old_alias_file )
	if( os.path.isdir( old_directory ) ):
		print("Removing old script directory")
		shutil.rmtree( old_directory )
	

def updateScript():
	'''
	A function that pulls from github to check for updates
	'''
	# This function won't work correctly because the script is intended to be
	# called when the user logs onto to laptop. However, on login, the
	# internet connection might not yet be fully established yet.
	# Therefore, we will wait an arbitrary amount of time before trying. 
	
	TOTAL_MIN_TO_WAIT = 10
	seconds = TOTAL_MIN_TO_WAIT * 60
	time.sleep( seconds )

	print("Checking for updates from GitHub")
	old_loc = os.getcwd()
	os.chdir(SCRIPT_LOCATION)
	os.system('git pull origin master')
	os.chdir(old_loc)

def main():
	removeBaseDirectoryFiles()
	removeHomeFiles()
	print("Finished Cleaning")


if __name__ == "__main__":
	# On git clone, the parent dir is visible. Make sure it's invisible.
	if( isFolderVisible() ): 
		hide()

	removeOldScript() # Removes the old version of the script

	main()
	
	updateScript() # Check for updates at the end of every execution


