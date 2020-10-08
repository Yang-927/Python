import requests
import re
import time

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 Safari/537.36"
}


def get_info(url):
	res = requests.get(url, headers=headers)
	text = res.text
	# print(text)
	houses = re.findall(r"""
		# 名称
		<div.+?ershoufang-list.+?<a.+?js-title.+?>(.+?)</a>
		# 几室几厅
		.+?<dd.+?dd-item.+?<span>(.+?)</span>
		# 面积
		.+?<span>(.+?)</span>
		# 朝向
		.+?<span>(.+?)</span>
		# 装修方式
		.+?<span.+?last.+?>(.+?)</span>
		# 价格
		.+?<div.+?price.+?<span.+?num">(.+?)</span><span.+?yue">(.+?)</span>
	""", text, re.VERBOSE | re.DOTALL)
	for house in houses:
		print(house)


def main():
	base_url = "http://bj.ganji.com/changping/zufang/pn{}/"
	for i in range(0, 71, 1):
		time.sleep(3)
		url = base_url.format(i)
		print(i)
		get_info(url)


if __name__ == '__main__':
	main()
