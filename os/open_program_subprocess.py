import subprocess

# shell argument = True if was want to run windows shell commamnds
# this can be a security hazard is we do not have trusted input (no user input)
# without shell argument, we would need to provide a list of commands to run
#subprocess.run('dir', shell=True)

# we must capture the stdout in order to save to variable (captured as bytes by default)
# python wil not throw exception if the external command fails; it only returns a non zero error code
p1 = subprocess.run(['dir','/q'], shell=True, capture_output=True)

print(p1.args)
print(p1.returncode)
print(p1.stdout)
print(p1.stdout.decode())

# return a string versus bytes by default (include EOL characters for word wrapping)
p1 = subprocess.run(['dir','/q'], shell=True, capture_output=True, text=True)
print(p1.stdout)

# stdout=subprocess.PIPE does what capture_output=True does in the background
p1 = subprocess.run(['dir','/q'], shell=True, stdout=subprocess.PIPE, text=True)
print(p1.stdout)

# write stdout to a file
#C:\Users\Corbin\PycharmProjects\file_mgmt\venv\Scripts

with open('output.txt', 'w') as f:
    p1 = subprocess.run(['dir', '/q'], shell=True, stdout=f, text=True)
    print(p1.returncode)
    print(p1.stderr)

p1 = subprocess.run(['type', 'output.txt'], shell=True, capture_output=True, text=True)

print(p1.stdout)
print(type(p1.stdout))

string = 'CORBINBLOCK'
#bytes_string = bytes(string, 'utf-8')
#print(type(bytes_string))

bytes_p1 = bytes(p1.stdout, 'utf-8')

# capture output from p1 and pass into p2
p2 = subprocess.run(['findstr', string], shell=True, capture_output=True, input=bytes_p1)

print(p2.stdout.decode())
