import subprocess

command = """
$host_name = $(hostname)
$host_name
"""

output = subprocess.run(["pwsh.exe", "-c", command], capture_output=True)

if "WIN-01-LENOVO" in output.stdout.decode('utf-8').split():
    print(subprocess.run("wsl -u root"))
elif "WIN-02-ASUS" in output.stdout.decode('utf-8').split():
    print(subprocess.run("wsl apt-get update && apt-get upgrade -y"))
elif "CBLOCKDYFX2X2" in output.stdout.decode('utf-8').split():
    print(subprocess.run("wsl apt-get update && apt-get upgrade -y"))
else:
    print('hostname not found!')
