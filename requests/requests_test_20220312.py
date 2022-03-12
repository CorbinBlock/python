import requests

r = requests.get('https://api.github.com/events')

r = requests.post('https://httpbin.org/post', data={'key': 'value'})
