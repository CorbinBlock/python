import zipfile

with zipfile.ZipFile('files.zip', 'w') as my_zip:
    my_zip.write('test.txt')
    my_zip.write('thumbnail.png')
