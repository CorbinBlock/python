#Setting up venv - Corey Schaffer
cd /home/corbinblock/git/python
#enable vim spell-check mode
#command mode
#run :set spell spelllang=en_us

#https://youtu.be/Kg1Yvry_Ydk
#set up virtual environment in order to retain the same version for packages and dependencies - so new updates will not break your code
#pip3 list - check pip packages
#apt-get install python3-venv
#python3 -m venv requests-project-venv
#activate venv

source /requests-project-venv/bin/activate
#validate activation by verifying if python source is venv version
#which python3 #not functioning yet
#venv name will now be in parenthesis in terminal to the left of  username@hostname
#pip list
#pip install requests
#FYI - do not name a python file requests.py - this will cause conflicts with the actual requests module/library!! :)

#exit python
#exit()

import requestsi
>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
401
>>> r.headers['content-type']
'application/json; charset=utf-8'
>>> r.encoding
'utf-8'
>>> r.text
'{"message":"Bad credentials. The API can\'t be accessed using username/password authentication. Please create a personal access token to access this endpoint: http://github.com/settings/tokens","documentation_url":"https://docs.github.com/articles/creating-a-personal-access-token-for-the-command-line"}'
>>> r.json()
{'message': "Bad credentials. The API can't be accessed using username/password authentication. Please create a personal access token to access this endpoint: http://github.com/settings/tokens", 'documentation_url': 'https://docs.github.com/articles/creating-a-personal-access-token-for-the-command-line'}
