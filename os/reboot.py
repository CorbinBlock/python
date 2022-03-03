import os
import sys

shell = "pwsh.exe"
option = "-c"
command = "Restart-Computer -ComputerName "
arg_one = sys.argv[1]
command_string = f" {shell} {option} {command} {arg_one}"
print(command_string)
os.system(command_string)
