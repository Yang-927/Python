import requests
import re

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 Safari/537.36"
}
def main():
	base_url = "https://www.qiushibaike.com/text/"
	res = requests.get(base_url, headers=headers)
	html = res.text
	texts = re.findall(r"""
		<div.+?typs_.+?author.+?<h2>\s(.+?)\s</h2>
		.+?<div.+?content.+?<span>\s(.+?)\s</span>
	""", html, re.VERBOSE | re.DOTALL)

	for text in texts:
		print(text)
		# text = re.sub("\w", '1', text)

if __name__ == '__main__':
    main()