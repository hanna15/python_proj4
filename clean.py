import argparse
import sys
from pathlib import Path
import re
import shutil

def createDirectories(folderset, matches):
	#print(foldernames)
	for folder in folderset:
		path = episodePath / folder.capitalize()
		if not path.exists():
			path.mkdir()

	for episode in matches:
		pathsToCheck = re.sub('\W','',str(episode)).lower() #clean path
		for foldername in folderset:
			if foldername in pathsToCheck: #check if the stringpath has the foldername in the path
				#if the path contains the name, move the file to the correct folder with corresponding foldername
				shutil.copy(str(episode), str(episodePath / foldername.capitalize()))

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
	(new_dir / 'movies').mkdir() #create dir for all moies
	(new_dir / 'music').mkdir() #create dir for all audio 

episodePath = new_dir / 'episodes'
moviePath = new_dir / 'movies'
musicPath = new_dir / 'music'

regexepisodes1 = '[sS][0-9]{1,2}[eE][0-9]{1,2}.*.avi'
#|[sS][0-9]{1,2}[eE][0-9]{1,2}.*.mp4' 
regexepisodes2 = '[Ss]eason[s]? [0-9].*.avi'
#'[Ss]eason[s]? [0-9]{1,}.*(.avi|.mp4)'
#'[Ss]eason[s]? [0-9].*.avi|Season [0-9].*.mp4'
notmatch = '^(?!.*'+regexepisodes1+').*$'
notmatch2 = '^(?!.*'+regexepisodes2+').*$'
regexmusic = '.*.mp3'
regexmovies = '.*.avi'

episodeMatches1 = []
for file in allFiles:
	if re.findall(regexepisodes1, str(file)):
		episodeMatches1.append(file)

episodenameset1 = set()
for episode in episodeMatches1:
	mess = re.split(r"/|\\", str(episode))[-1]
	newname = re.sub(regexepisodes1 +'|\W','',mess)
	if newname:
		episodenameset1.add(newname.lower())
createDirectories(episodenameset1, episodeMatches1)

episodesMatches2 = []
for file in allFiles:
	if re.findall(regexepisodes2, str(file)):
		if re.findall(notmatch, str(file)):
			episodesMatches2.append(file)

episodenameset2 = set()
for episode in episodesMatches2:
	mess = str(episode).split('downloads')[-1] 
	clean = re.sub('\W', '', mess).lower()
	foldername = re.sub('season.*', '', clean)
	episodenameset2.add(foldername)
createDirectories(episodenameset2, episodesMatches2)

for file in allFiles:
	if re.findall(".*.avi", str(file)):
		if re.findall(notmatch, str(file)):
			if re.findall(notmatch2, str(file)):
				if re.findall('[0-9]{4}', str(file)):
					shutil.copy(str(file), str(moviePath))

for file in allFiles: 
	if re.findall(regexmusic, str(file)):
		shutil.copy(str(file), str(musicPath)) #copy music files

p = Path().resolve() / dest
sortedFiles = list(p.glob("**/*"))

print(len(allFiles))
print(len(sortedFiles))


#DUMP
#list = [str(i) for i in allFiles]
#for i in sorted(list, key= lambda x: x[-3:]):
#	print(i)



 


