import os
  
# This is to get the directory that the program 
# is currently running in.
dir_path = "/home/ec2-user/environment/"
  
for root, dirs, files in os.walk(dir_path):
    for file in files: 
        # change the extension to 
        # the one of your choice.
        if file.endswith(''):
            print (root+'/'+str(file))