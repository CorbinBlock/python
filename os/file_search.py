import os 
from datetime import datetime

os.chdir('/home/')

print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)



print(os.path.basename('tmp/test.txt'))
print(os.path.basename('tmp/test.txt'))
print(os.path.dirname('tmp/test.txt'))


print(os.path.split('tmp/test.txt'))
print(os.path.splitext('tmp/test.txt'))


#for dirpath, dirnames, filenames in os.walk('/home/'):
#    print(‘Current Path:’, dirpath)
#    print(‘Directories:’, dirnames)
#    print(‘Files:’, filenames)
#    print()
