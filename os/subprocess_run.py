import subprocess

command = """
$host_name = $(hostname)
$host_name

"""

output = subprocess.run(["pwsh.exe", "-c", command], capture_output=True)
# output = subprocess.run(["pwsh.exe", "-c", command], stdout=subprocess.PIPE, text=True)

# print(type(str(output)))

# output == str(output)
# print(output)

output == output.stdout.decode('utf-8')
if "WIN-01-LENOVO" in output.stdout.decode('utf-8').split():
     print(output)

# if output == 'WIN-01-LENOVO':
#     print(output)
