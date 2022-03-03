import os

shell = "pwsh.exe"
option = "-c"
command = 'Get-Batch'
command_string = f" {shell} {option} {command}"
print(command_string)
os.system(command_string)
