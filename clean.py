import argparse
import sys
from pathlib import Path
import re
parser = argparse.ArgumentParser(
	description="Clean download folder")

parser.add_argument("downl_folder", metavar="FOLDER", type=str, help="the folder to be cleaned")
parser.add_argument("dest_folder", metavar="FOLDER", type=str, help="the destination folder")

args = parser.parse_args()
downl = args.downl_folder
dest = args.dest_folder
p = Path().resolve() / downl
result = list(p.glob("**/*.avi"))
for i in result:
	print()
print(downl)
print(dest)
#print(p)

#def test(downl, dest):

#	print(downl)
#	print(dest)




