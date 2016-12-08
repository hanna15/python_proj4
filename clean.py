import argparse
import sys
from pathlib import Path
import re
import shutil

parser = argparse.ArgumentParser(
	description="Clean download folder")

parser.add_argument("downl_folder", metavar="FOLDER", type=str, help="the folder to be cleaned")
parser.add_argument("dest_folder", metavar="FOLDER", type=str, help="the destination folder")

args = parser.parse_args()
downl = args.downl_folder
dest = args.dest_folder
p = Path().resolve() / downl
allFiles = list(p.glob("**/*")) #get all files

new_dir = Path().resolve() / dest 
if not new_dir.exists():
	new_dir.mkdir()
	(new_dir / 'episodes').mkdir() #create dir for all episodes
	(new_dir / 'moives').mkdir() #create dir for all moies

episodePath = new_dir / 'episodes'
moviePath = new_dir / 'movies'

regexepisodes = '[sS][0-9]{1,2}[eE][0-9]{1,2}.*.avi' #all episodes that have number and .avi
regexepisodes2 = 'Season [0-9].*.avi'
notmatch = '^(?!.*'+regexepisodes+').*$'

episodeMatches = []
for file in allFiles:
	if re.findall(regexepisodes, str(file)):
		episodeMatches.append(file)

################new matcc
#TODO - create functions <3
episodesMatches2 = []
for file in allFiles:
	if re.findall(regexepisodes2, str(file)):
		if re.findall(notmatch, str(file)):
			episodesMatches2.append(file)

foldernames = set()
for episode in episodesMatches2:
	mess = str(episode).split('downloads')[-1] 
	clean = re.sub('\W', '', mess).lower()
	foldername = re.sub('season.*', '', clean)
	foldernames.add(foldername)
#print(foldernames)
for folder in foldernames:
	path = episodePath / folder.capitalize()
	if not path.exists():
		path.mkdir()

for episode in episodesMatches2:
	pathsToCheck = re.sub('\W','',str(episode)).lower() #clean path
	for foldername in foldernames:
		if foldername in pathsToCheck: #check if the stringpath has the foldername in the path
			#if the path contains the name, move the file to the correct folder with corresponding foldername
			shutil.copy(str(episode), str(episodePath / foldername.capitalize()))

####################

untrackedPath = episodePath / 'UntrackedEpisodes'
for match in episodeMatches:
	if not untrackedPath.exists():
		untrackedPath.mkdir()
	shutil.copy(str(match), str(untrackedPath))

allepisodes = list(untrackedPath.glob('**/*')) 
splittedFilenames = []
for episode in allepisodes:
	splittedFilenames.append((re.split(r"/|\\", str(episode)))[-1])

#TODO- sameina lykkjur
nameset = set() #set of foldernames for episodes
for shortfilename in splittedFilenames:
	newname = re.sub(regexepisodes +'|\W','',shortfilename)
	if newname:
		nameset.add(newname.lower())

for foldername in nameset: #create dir for common episodes
	subepisodePath = episodePath / foldername.capitalize()
	if not subepisodePath.exists():
		subepisodePath.mkdir()

for episode in allepisodes:
	pathsToCheck = re.sub('\W','',str(episode)).lower() #clean path
	for foldername in nameset:
		if foldername in pathsToCheck: #check if the stringpath has the foldername in the path
			#if the path contains the name, move the file to the correct folder with corresponding foldername
			shutil.copy(str(episode), str(episodePath / foldername.capitalize()))

#DUMP
#list = [str(i) for i in allFiles]
#for i in sorted(list, key= lambda x: x[-3:]):
#	print(i)



 


