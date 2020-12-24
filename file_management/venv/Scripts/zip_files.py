import os
import sys
import zipfile

def zip_func(arg1, arg2):
    argOne= sys.argv[1]
    argTwo= sys.argv[2]
    fileNameNoExt  = argOne.replace('.txt','')
    zipName= '.zip'
    zipName= fileNameNoExt + zipName
    print(argOne)
    print(zipName)
    print(argTwo)
    os.chdir(argTwo)
    with zipfile.ZipFile(zipName, 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
        my_zip.write(argOne)
    os.remove(argOne)


if __name__ == '__main__':
    # zip_files.py executed as script
    # do something
    zip_func(sys.argv[1], sys.argv[2])


