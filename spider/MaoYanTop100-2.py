import requests
import re
from lxml import etree
import json
import time

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 Safari/537.36",
	"Cookie": "__mta=216317865.1602041250463.1602051124545.1602051153589.18; _lxsdk_cuid=174d3810094c8-025512ba39e44b-6a54732e-100200-174d3810094c0; uuid_n_v=v1; uuid=07EC6910084D11EB9FC34F90BE550CA8BCC9998B4859452DB8C518CDC5663D21; _lxsdk=07EC6910084D11EB9FC34F90BE550CA8BCC9998B4859452DB8C518CDC5663D21; _csrf=6af46c1233a9e404ff51d976d89f9227be27eaa25db866a6196c9760ff34379d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1602041250,1602048734; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1602051153; _lxsdk_s=175018bb4c9-660-d16-734%7C%7C36"
}

infos = []


def get_info(url):
	res = requests.get(url, headers=headers)
	text = res.content.decode('utf-8')
	html = etree.HTML(text)
	dls = html.xpath("//dd")
	for i in dls:
		list_l = {}
		name = i.xpath(
			'./div[@class="board-item-main"]/div[@class="board-item-content"]/div[@class="movie-item-info"]/p[@class="name"]/a/text()')
		star = i.xpath(
			'./div[@class="board-item-main"]/div[@class="board-item-content"]/div[@class="movie-item-info"]/p[@class="star"]/text()')
		scoreOne = i.xpath(
			'./div[@class="board-item-main"]/div[@class="board-item-content"]/div[@class="movie-item-number score-num"]/p[@class="score"]/i[@class="integer"]/text()')
		scoreTow = i.xpath(
			'./div[@class="board-item-main"]/div[@class="board-item-content"]/div[@class="movie-item-number score-num"]/p[@class="score"]/i[@class="fraction"]/text()')

		list_l["name"] = ''.join(name)
		star = ''.join(star)
		list_l["star"] = re.sub(r'\s', '', star)
		list_l["score"] = ''.join(scoreOne) + ''.join(scoreTow)
		infos.append(list_l)
	return infos


def main():
	base_url = 'https://maoyan.com/board/4?offset={}'
	for i in range(0, 91, 10):
		time.sleep(5)
		url = base_url.format(i)
		print(i)
		info = get_info(url)
		with open('./MaoYan1.json', 'w', encoding='utf-8') as f:
			json.dump(info, f, ensure_ascii=False)
		print(info)


if __name__ == '__main__':
	main()
