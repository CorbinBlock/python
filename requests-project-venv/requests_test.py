import requests
r = requests.get('https://www.ozk.com/login/', auth=('user', 'pass'))
r.status_code
r.text

#write requests object to file 
#source - https://stackoverflow.com/questions/14114729/save-a-large-file-using-the-python-requests-library

# Throw an error for bad status codes
r.raise_for_status()

with open('output.html', 'wb') as handle:
    for block in r.iter_content(1024):
            handle.write(block)

#print the attributes and methods associated with an object. in this example we are examining the response object from the request library

print(dir(r))
