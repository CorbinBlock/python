import os

shell = "pwsh.exe"
option = "-c"
command = "Restart-Computer -ComputerName WIN-01-LENOVO"
command_string = f" {shell} {option} {command}"
os.system(command_string)