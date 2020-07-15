from requests_html import HTMLSession
session = HTMLSession()
r = session.get('https://chiasenhac.vn/tim-kiem?q=how+you+like+that')
rs = r.html.find('.media-title a',first = False)
# for x in rs:
#     print(x.attrs['title'] + ": \t\t\t\t" +x.attrs['href'] )
rss = r.html.find('.author .media',first = False)
# for x in rs:
#     print(x.attrs['title'] + ": " + x.attrs['href'])
for x in rss:
    print(x)