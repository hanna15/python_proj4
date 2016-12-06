import argparse
import sys

parser = argparse.ArgumentParser(
	description="Clean download folder")

parser.add_argument("downl_folder", metavar="FOLDER", type=str, help="the folder to be cleaned")
parser.add_argument("dest_folder", metavar="FOLDER", type=str, help="the destination folder")

def test(args.downl_folder, args.dest_folder):
	downl = args.downl_folder
	dest = args.dest_folder
	print(downl)
	print(dest)




