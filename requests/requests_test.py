import requests

#write requests object to file 
#source - https://stackoverflow.com/questions/14114729/save-a-large-file-using-the-python-requests-library

#print the attributes and methods associated with an object. in this example we are examining the response object from the request library




response = requests.get('https://ozk.com/login/', stream=True)

# Throw an error for bad status codes
response.raise_for_status()

with open('output.html', 'wb') as handle:
        for block in response.iter_content(1024):
                    handle.write(block)

response.text


print(dir(response))
