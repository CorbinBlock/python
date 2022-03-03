import os

shell = "pwsh.exe"
option = "-c"
command = 'wsl apt-get update && wsl apt-get upgrade -y'
command_string = f" {shell} {option} {command}"
print(command_string)
os.system(command_string)