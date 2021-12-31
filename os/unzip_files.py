import os
import sys
import zipfile

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
