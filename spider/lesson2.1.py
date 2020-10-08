from urllib import request

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 Safari/537.36 "
}

res = request.Request('http://piaofang.maoyan.com/dashboard', headers=headers)
print(request.urlopen(res).read())
