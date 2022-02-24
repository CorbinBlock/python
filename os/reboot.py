import os

# cmd
# command = "shutdown /r"
path_dir: str = r"C:\Users\Administrator"

#pwsh
command = "pwsh.exe -c ls {}".format(path_dir)



os.system(command)