import os

shell = "pwsh.exe"
option = "-c"
command = "Get-Creds admin; Enter-RDP"
command_string = f" {shell} {option} {command}"
print(command_string)
os.system(command_string)
