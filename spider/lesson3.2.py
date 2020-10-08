from urllib import request
from http.cookiejar import MozillaCookieJar

cookiejar = MozillaCookieJar('cookie.txt')

cookiejar.load()

handler = request.HTTPCookieProcessor(cookiejar)

opener = request.build_opener(handler)

res = opener.open('http://httpbin.org/cookies/set/score/100')

for i in cookiejar:
	print(i)