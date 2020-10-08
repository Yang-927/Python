# import requests
#
# url = 'http://httpbin.org/ip'
#
# proxy = {
# 	'http': 'http://61.163.32.88:3128'
# }
#
# res = requests.post(url,proxies=proxy)
#
# print(res.text)


# 获取Cookie
# import requests
# #
# # url = 'https://www.baidu.com'
# #
# # res = requests.get(url)
# #
# # print(res.cookies.get_dict())

# requests的session应用
import requests

post_url = 'https://i.meishi.cc/login_t.php?username=13703320391&login_type=2&password=FVictory98&cookietime=on'
post_data = {
	'username': "13703320391",
	'password': 'FVictory98'
}

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 Safari/537.36"
}

session = requests.session()
session.post(post_url,headers=headers,data=post_data)

url = 'https://i.meishi.cc/cook.php?id=14287458'
res = session.get(url)

print(res.text)
