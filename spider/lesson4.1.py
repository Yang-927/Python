import requests

url = 'https://i.meishi.cc/login_t.php'

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 Safari/537.36"
}

data = {
	'username': "13703320391",
	'password': 'FVictory98',
	'login_type': '2',
	'cookietime': 'on'
}

res = requests.post(data=data,url=url,headers=headers)

print(res.encoding)