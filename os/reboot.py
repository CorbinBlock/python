import os
import sys

shell = "pwsh.exe"
option = "-c"
command = "Restart-Computer -ComputerName $(hostname)"
command_string = f" {shell} {option} {command}"
print(command_string)
os.system(command_string)
