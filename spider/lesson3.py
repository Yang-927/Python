# from urllib import request
#
# url = 'http://httpbin.org/ip'
# # 没有代理
# # res = request.urlopen(url);
# # print(res.read())
#
# # 使用代理
# handler = request.ProxyHandler({'http': "61.163.32.88:3128"})
#
# opener = request.build_opener(handler)
# res = opener.open(url)
# print(res.read())

# cookiejar模块应用
from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

# 创建CookieJar对象
cj = CookieJar();
# 使用CookieJar生成HTTPCookieProcessor对象
handler = request.HTTPCookieProcessor(cj)
# 使用handler创建一个opener
opener = request.build_opener(handler)
# 使用opener发送登录请求
post_url = 'https://i.meishi.cc/login_t.php?username=13703320391&login_type=2&password=FVictory98&cookietime=on'
post_data = parse.urlencode({
	'username': "13703320391",
	'password': 'FVictory98'
})
req = request.Request(post_url,data=post_data.encode('utf-8'))
res = opener.open(req)
print(res.read().decode('utf-8'))

post_url2 = 'https://i.meishi.cc/cook.php?id=14287458'
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 Safari/537.36"
}

res = request.Request(post_url2)

print(res.read().decode('utf-8'))