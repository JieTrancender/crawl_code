# import urllib.request

# response = urllib.request.urlopen('https://www.python.org')
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))


# import urllib.parse
# import urllib.request

# data = bytes(urllib.parse.urlencode({'name': 'germey'}), encoding='utf-8')
# response = urllib.request.urlopen('https://www.httpbin.org/post', data = data)
# print(response.read().decode('utf-8'))


# import urllib.request

# response = urllib.request.urlopen('https://www.httpbin.ogr/get', timeout = 0.1)
# print(response.read())


# import socket
# import urllib.request
# import urllib.error

# try:
#     response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')


# import urllib.request

# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))


# from urllib import request, parse

# url = 'https://www.httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT',
#     'Host': 'www.httpbin.org'
# }
# dict = {'name': 'germey'}
# data = bytes(parse.urlencode(dict), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))


# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError

# username = 'admin'
# password = 'admin'
# url = 'https://ssr3.scrape.center/'

# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)

# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)


# import http.cookiejar, urllib.request

# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# for item in cookie:
#     print(item.name + "=" + item.value)


# import urllib.request, http.cookiejar

# filename = 'cookie.txt'
# # cookie = http.cookiejar.MozillaCookieJar(filename)
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)


# import urllib.request, http.cookiejar

# filename = 'cookie.txt'
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load(filename, ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# print(response.read().decode('utf-8'))
