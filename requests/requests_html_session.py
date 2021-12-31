from requests_html import HTML, HTMLSession

session = HTMLSession()
r = session.get('https://coreyms.com/')


article = r.html.find('article', first=True)

headline = article.find('.entry-title-link', first=True).text
print(headline)

summary = article.find('.entry-content p', first=True).text
print(summary)

#vid_src = article.find('iframe', first=True).html
#print(vid_src)

#parse embedded youtube URL
vid_src = article.find('iframe', first=True).attrs['src']
print(vid_src)


#parse videoid from youtube URL string
#print list of values in our string split by a forward flash
#vid_id = vid_src.split('/')
#print(vid_id)

#return fourth index in list
vid_id = vid_src.split('/')[4]
print(vid_id)

#now split with question mark('?') as the delimiter (this returns the URL perfectly)
#vid_id = vid_src.split('?')[0]
#print(vid_id)

#now split with question mark('?') as the delimiter (video id)
vid_id = vid_id.split('?')[0]
print(vid_id)

yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)
