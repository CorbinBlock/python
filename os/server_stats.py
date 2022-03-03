import os

shell = "pwsh.exe"
option = "-c"
command = "Get-CPUsage; Get-LastBootTime; Get-MemoryUsage"
command_string = f" {shell} {option} {command}"
os.system(command_string)