import subprocess
from sys import platform

command = """
hostname
"""

debian_command = """
apt-get update && apt-get upgrade -y
cd /git/python && git pull --no-rebase
"""

fedora_command = """
dnf upgrade -y
cd /git/python && git pull --no-rebase
"""
option = "-c"

powershell = "pwsh.exe"

shell = "/bin/bash"

wsl_command = 'bash -c "apt-get update && apt-get upgrade -y && cd /git/python && git pull --no-rebase"'

if platform == "linux" or platform == "linux2":
    print(f" {platform} server detected!")
    output = subprocess.run([shell, option, command], capture_output=True)
    if "WIN-01-LENOVO" in output.stdout.decode('utf-8').split():
        print(subprocess.run([shell, option, debian_command]))
    elif "WIN-02-ASUS" in output.stdout.decode('utf-8').split():
        print(subprocess.run([shell, option, debian_command]))
    elif "CBLOCKDYFX2X2" in output.stdout.decode('utf-8').split():
        print(subprocess.run([shell, option, debian_command]))
    elif "UNIX-01-DEBIAN" in output.stdout.decode('utf-8').split():
        print(subprocess.run([shell, option, debian_command]))
    elif "UNIX-02-FEDORA" in output.stdout.decode('utf-8').split():
        print(subprocess.run([shell, option, fedora_command]))
    else:
        print('hostname not found!')
elif platform == "win32":
    print(f" {platform} server detected!")
    output = subprocess.run([powershell, option, command], capture_output=True)
    if "WIN-01-LENOVO" in output.stdout.decode('utf-8').split():
        print(f"{debian_command}")
        print(subprocess.run("wsl -u root"))
    elif "WIN-02-ASUS" in output.stdout.decode('utf-8').split():
        print(subprocess.run(wsl_command))
    elif "CBLOCKDYFX2X2" in output.stdout.decode('utf-8').split():
        print(subprocess.run(wsl_command))
        # print(subprocess.run(wsl_command))
    else:
        print('hostname not found!')
else:
    print(f" {platform} server detected! Please check server.")

