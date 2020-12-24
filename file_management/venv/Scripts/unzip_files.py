import os
import sys
import zipfile

def unzip_func(arg1, arg2):
	argOne= sys.argv[1]
	argTwo= sys.argv[2]
	os.chdir(argTwo)
	fileName =  argOne
	print(os.getcwd())
	print(argTwo)
	print(fileName)
	with zipfile.ZipFile(fileName, 'r') as zip_ref:
		zip_ref.printdir()
		zip_ref.extractall()
	os.remove(argOne)

if __name__ == '__main__':
    # unzip_files.py executed as script
    # do something
    unzip_func(sys.argv[1], sys.argv[2])