import requests

r = requests.get('https://api.github.com/events')
print(r)

r = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(r)