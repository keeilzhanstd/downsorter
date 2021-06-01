from os import listdir
from os.path import isfile, join
import shutil

path = "C:\\Users\\depsp\\Downloads"
files = [f for f in listdir(path) if isfile(join(path, f))]

extensions = {
	"pdf": ['pdf'], 
	"images": ['png', 'jpeg', 'jpg', 'bmp', 'svg'],
	"videos": ['mp4', 'vla'],
	"docs": ['docx', 'xlsx', 'doc', 'xls', 'txt'],
	"exe": ['exe'],
	"prog": ['c', 'cpp', 'py', 'swift', 'js', 'html', 'css'],
	"zips": ['rar', '7z', 'zip']
	}

for file in files:
	tmp = ""
	for i in file[-1:0:-1]:
		if i == ".":
			break
		else:
			tmp += i
	extension = tmp[-1::-1]
	if extension in extensions["pdf"]:
		shutil.move(path+"/"+file, path+"/pdf")
	elif extension in extensions["images"]:
		shutil.move(path+"/"+file, path+"/images")
	elif extension in extensions["videos"]:
		shutil.move(path+"/"+file, path+"/videos")
	elif extension in extensions["docs"]:
		shutil.move(path+"/"+file, path+"/docs")
	elif extension in extensions["exe"]:
		shutil.move(path+"/"+file, path+"/exe")
	elif extension in extensions["prog"]:
		shutil.move(path+"/"+file, path+"/prog")
	elif extension in extensions["zips"]:
		shutil.move(path+"/"+file, path+"/zips")
	else:
		shutil.move(path+"/"+file, path+"/other")	
