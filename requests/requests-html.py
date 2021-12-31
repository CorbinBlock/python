
from requests_html import HTML

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    
articles = html.find('div.article')

#for article in articles:
#    headline = article.find('h2', first=True).text
#   summmary = article.find('p', first=True).text
#   print(headline)
#   print(summary)
#   print()
