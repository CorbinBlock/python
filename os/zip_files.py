import os
import sys
import zipfile

argOne= sys.argv[1]
argTwo= sys.argv[2]

fileNameNoExt  = argOne.replace('.txt','')
zipName= '.zip'
zipName= fileNameNoExt + zipName

print(argOne)
print(zipName)
print(argTwo)
os.chdir(argTwo)

with zipfile.ZipFile(zipName, 'w') as my_zip:
        my_zip.write(argOne)

os.remove(argOne)
