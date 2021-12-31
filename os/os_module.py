import os

print(dir(os))

print(os.getcwd())

os.chdir('/home/corbinblock/git/python/util_python')


os.rmdir('os_demo')
os.mkdir('os_demo')


#os.removedirs('os_demo/os_demo2')
os.makedirs('os_demo/os_demo2')



print(os.listdir())


