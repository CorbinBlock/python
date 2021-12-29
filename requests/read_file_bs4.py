from bs4 import BeautifulSoup

htmltxt = "<p>Hello World</p>"
soup = BeautifulSoup(htmltxt, 'lxml')
type(soup)
# bs4.BeautifulSoup
soup.text
# 'Hello World'
soup = BeautifulSoup("""<h1>Hello</h1><p>World</p>""", 'lxml')
soup.text
# 'HelloWorld'i
mytxt = """
<h1>Hello World</h1>
<p>This is a <a href="http://example.com">link</a></p>"""

soup = BeautifulSoup(mytxt, 'lxml')
soup.text
# 'Hello World\nThis is a link'
mytxt = """
<h1>Hello World</h1>
<p>This is a <a href="http://example.com">link</a></p>
"""
soup = BeautifulSoup(mytxt, 'lxml')
soup.find('a')
# <a href="http://example.com">link</a>
