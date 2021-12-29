import csv
from requests_html import HTML, HTMLSession

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)
#    html.render() #execute format error? this might break code because raspberry pi is arm64??

match = html.find('#footer', first=True)
print(match.html)
