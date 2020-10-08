from urllib import request
from http.cookiejar import MozillaCookieJar

# MozillaCookieJar应用-保存一个网站的Cookie
cookiejar = MozillaCookieJar();

handler = request.HTTPCookieProcessor(cookiejar)

opener = request.build_opener(handler)

res = opener.open('https://www.baidu.com')

cookiejar.save('cookie.txt')
