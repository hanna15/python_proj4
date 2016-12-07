# Assignment 4

## Short description of the script
The script organizes the files in the download folder to episodes, movies and music. Unsorted files from the download folder are put in special directory called unsorted in the destination folder. 
The episodes in the episode folder are divided into folders by name of the episode and then further into folders by season if possible. 

The script handles the most generelized file formats but does not go deep in special cases. 

Episodes in the episode folder are renamed if the file name contains some unnecessary text. The text is removed from the filename. 
The desired solution was to erase all unnecessary text beetween the episode name and number to the file ending. But it conflicted with some of the file names so this bug was fixed with the solution described above.

All known junk files are deleted from the download folder so that they will not be a part of the unsorted files in the destination folder.

When each file is copied from the download folder to the destination folder it is removed from the download folder.

Finally when all the files have been removed from the download folder to the destination folder the empty paths are deleted from the download folder so it will be empty in the end.

+ No PyPI packages are needed nor any dependencies. 

## How to run the script
+ Make sure that Python3 is installed
+ Unzip the project to your favorite directory
+ Run the script in your favorite command line window:

### mac:
python3 clean.py /Path/to/the/downloadfolder
/Path/To/desired/destination

### windows:
py clean.py /Path/to/the/downloadfolder
/Path/To/desired/destination
 



