import argparse
import sys
from pathlib import Path
import re
import shutil

def createDirectories(folderset, matches):
	for folder in folderset:
		path = episodePath / folder.capitalize()
		if not path.exists():
			path.mkdir()

	for episode in matches:
		pathsToCheck = re.sub('\W','',str(episode)).lower() #clean path
		for foldername in folderset:
			if foldername in pathsToCheck: #check if the stringpath has the foldername in the path
				#if the path contains the name, move the file to the correct folder with corresponding foldername
				if episode.exists():
					shutil.copy(str(episode), str(episodePath / foldername.capitalize()))
					episode.unlink()

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

#regex strings
regexepisodes1 = '[sS][0-9]{1,2}[eE][0-9]{1,2}.*\.(avi|mp4|mkv)$'
regexepisodes2 = '[Ss]eason[s]? [0-9].*\.(avi|mkv)$'

notmatch = '^(?!.*'+regexepisodes1+').*$'
notmatch2 = '^(?!.*'+regexepisodes2+').*$'

regexmusic = '.*\.mp3$'
regexmovies = '.*\.(avi|mp4|mkv)$'

regexseason1 = '[sS][0-9]{1,2}[eE][0-9]{1,2}'
regexseason2 =  '[Ss]eason[s]? [0-9]'

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
	if re.findall(regexmovies, str(file)):
		if re.findall(notmatch, str(file)):
			if re.findall(notmatch2, str(file)):
				if re.findall('[0-9]{4}', str(file)):
					shutil.copy(str(file), str(moviePath))
					file.unlink() #delete file in download

for file in allFiles: 
	if re.findall(regexmusic, str(file)):
		shutil.copy(str(file), str(musicPath)) #copy music files
		file.unlink() #delete file in download

#create season folders for episodes
episodeFolder = list(episodePath.glob("*"))
for episodedir in episodeFolder:
	folderitems = list(episodedir.glob("*"))
	for item in folderitems:
		if re.findall(regexseason1, str(item)):
			dirtynumber = re.findall('[sS][0-9]{1,}', str(item))
			number = dirtynumber[0][1:]
			if number[0] == '0':
				number = number[1:]
			snr = 'Season ' + number
			new_season_path = episodedir / snr
			if not new_season_path.exists():
				new_season_path.mkdir()
			shutil.copy(str(item), str(new_season_path))
			item.unlink()

#rename file containing hdtv.xvid or xvid
regexjunk = r'[Hh][dD][Tt][Vv]\.[Xx][Vv][Ii][dD]|[Xx][Vv][Ii][dD]'
seasonstuff = list(episodePath.glob('*/*'))
for path in seasonstuff:
	if path.is_dir():
		episodes = list(path.glob('*'))
		for episode in episodes:
			if re.findall(regexjunk, str(episode)):

				t = re.sub(regexjunk, '', str(episode))
				target = Path(t)
	
				episode.rename(target)
				if episode.exists():
					episode.unlink()


#delete useless files from download folder
junk = '.*\.(txt|jpg|nfo|png)$'
for file in allFiles:
	if re.findall(junk, str(file)):
		file.unlink()

#move unorted files to destination folder and remove them from download folder
unsortedPath = new_dir / 'unsorted'
if not unsortedPath.exists():
	unsortedPath.mkdir()

#copy all unsorted files to unsorted folder in destination
restFiles = list(p.glob("**/*")) 
for file in restFiles:
	if not file.is_dir() and file.exists():
		shutil.copy(str(file), str(unsortedPath))
		file.unlink()

#remove all empty directories from downl
emptyFolders = list(p.glob("*"))
for folder in emptyFolders:
	shutil.rmtree(str(folder))

 


