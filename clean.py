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
result = list(p.glob("**/*"))

new_dir = Path().resolve() / dest
if not new_dir.exists():
	new_dir.mkdir()
	(new_dir / 'episodes').mkdir()
	(new_dir / 'moives').mkdir()

e = new_dir / 'episodes'
m = new_dir / 'movies'

#test with big bang theory
for i in result:
	if re.findall('(The.Big.Bang.Theory)(.*avi)', str(i)):
		big_bang = e / 'The_Big_Bang_Theory'
		if not big_bang.exists():
			big_bang.mkdir()

		if i.is_file():
			shutil.copy(str(i), str(big_bang))







#for i in result:
#	print(i)

	
#print(p)
#print(result)
#print(down)
#print(dest)
#print
#def test(downl, dest):

#	print(downl)
#	print(dest)




