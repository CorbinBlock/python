import os

shell = "pwsh.exe"
option = "-c"
command = "Enter-TuxGuitar; Enter-Reaper"
command_string = f" {shell} {option} {command}"
print(command_string)
os.system(command_string)
