import subprocess
from sys import platform

command = """
hostname
"""

if platform == "linux" or platform == "linux2":
    print(f" {platform} server detected!")
    output = subprocess.run(["/bin/bash", "-c", command], capture_output=True)
elif platform == "win32":
    print(f" {platform} server detected!")
    output = subprocess.run(["pwsh.exe", "-c", command], capture_output=True)
else:
    print(f" {platform} server detected! Please check server.")

if "WIN-01-LENOVO" in output.stdout.decode('utf-8').split():
    print("apt-get update && apt-get upgrade -y && exit")
    print(subprocess.run("wsl -u root"))
elif "WIN-02-ASUS" in output.stdout.decode('utf-8').split():
    print(subprocess.run("wsl apt-get update && apt-get upgrade -y"))
elif "CBLOCKDYFX2X2" in output.stdout.decode('utf-8').split():
    print(subprocess.run("wsl apt-get update && apt-get upgrade -y"))
else:
    print('hostname not found!')
