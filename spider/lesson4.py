import requests

url = 'https://www.baidu.com/s'

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 Safari/537.36"
}

# 字典
data = {
	'wd':'中国'
}

res = requests.get(url=url,params=data,headers=headers)
# 返回Unicode类型
# print(res.text)

# print(res.content.decode('utf-8'))

# print(res.url)

print(res.encoding)