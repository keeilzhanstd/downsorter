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
	for xt in extensions.keys():
		if extension in extensions[xt]:
			shutil.move(path+"/"+file, path+f'/{xt}')