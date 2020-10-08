import requests
from bs4 import BeautifulSoup
import time

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 Safari/537.36"
}


def get_detail_urls(url):
	res = requests.get(url, headers=headers)
	html = res.content.decode('utf-8')
	soup = BeautifulSoup(html, 'lxml')
	lis = soup.find('ol', class_='grid_view').find_all('li')
	detail_urls = []
	for li in lis:
		detail_url = li.find('a')['href']
		detail_urls.append(detail_url)
	return detail_urls


def parse_detail_url(detail_url):
	res = requests.get(detail_url, headers=headers)
	html = res.content.decode('utf-8')
	soup = BeautifulSoup(html, 'lxml')
	# infos = {}
	name = list(soup.find('div', id='wrapper').find('div', id='content').find('h1').stripped_strings)
	# name = soup.find('h1').find("span").get_text().replace(r'\r\n', '').strip()
	# info = soup.find('div', id='info')
	# director =
	name = ''.join(name)
	score = soup.find('strong', class_='ll rating_num').string
	time.sleep(2)
	write_str = "{} {}".format(name, score)

	# infos['剧名'] = name
	# infos['评分'] = score
	print(name)
	return write_str

def main():
	base_url = "https://movie.douban.com/top250?start={}&filter="
	# r 打开只读文件。a 以追加的文件打开文件，文件没有则创建。w 以写的方式打开文件，文件没有则创建。
	with open('./top250.csv', 'a', encoding='utf-8_sig') as f:
		for i in range(0, 251, 25):
			url = base_url.format(i)
			detail_urls = get_detail_urls(url)
			for detail_url in detail_urls:
				write_str = parse_detail_url(detail_url)
				f.write(write_str+"\n")
				f.flush()
	f.close()

if __name__ == '__main__':
	main()
