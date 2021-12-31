import requests

#This URL will be the URL that your login form points to with the "action" tag.
POST_LOGIN_URL = 'https://my.freecycle.org/login'

#This URL is the page you actually want to pull down with requests.
REQUEST_URL = 'https://my.freecycle.org/home/posts'

payload = {
    'username-input-name': '',
	'password-input-name': ''  #Preferably set your password in an env variable and sub it in.
}

with requests.Session() as session:
    post = session.post(POST_LOGIN_URL, data=payload)
    r = session.get(REQUEST_URL)
    print(r.text)   #or whatever else you want to do with the request data
