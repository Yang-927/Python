import requests
import re
from bs4 import BeautifulSoup
import json

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 Safari/537.36",
	"Cookie": "__mta=216317865.1602041250463.1602051040930.1602051042972.12; _lxsdk_cuid=174d3810094c8-025512ba39e44b-6a54732e-100200-174d3810094c0; uuid_n_v=v1; uuid=07EC6910084D11EB9FC34F90BE550CA8BCC9998B4859452DB8C518CDC5663D21; _lxsdk=07EC6910084D11EB9FC34F90BE550CA8BCC9998B4859452DB8C518CDC5663D21; _csrf=6af46c1233a9e404ff51d976d89f9227be27eaa25db866a6196c9760ff34379d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1602041250,1602048734; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1602051043; _lxsdk_s=175018bb4c9-660-d16-734%7C%7C24"

}

m_list = []


def get_detail_url(url):
	res = requests.get(url, headers=headers)
	text = res.content.decode('utf-8')
	# print(text)
	houses = re.findall(r"""
        <dd.+?name.+?<a.+?>(.+?)</a> #名
        .+?<p.+?star">\n\s+(.+?)\n\s+</p>  #主演
        .+?<p.+?releasetime">(.+?)</p>   #上映时间
        .+?<p.+?score.+?<i.+?integer">(.+?)</i><i.+?fraction">(.+?)</i> #评分
    """, text, re.VERBOSE | re.DOTALL)
	for house in houses:
		movie = {}
		movie['name'] = house[0]
		movie['act'] = house[1]
		movie['time'] = house[2]
		movie['grade'] = house[3] + house[4]
		m_list.append(movie)
	return m_list


def main():
	url = 'https://maoyan.com/board/4?offset={}'
	for i in range(0, 91, 10):
		base_url = url.format(i)
		detail_urls = get_detail_url(base_url)
		print(detail_urls)
		with open('MaoYan.json', 'a', encoding='utf-8') as f:
			json.dump(detail_urls, f, ensure_ascii=False)


# print(json.load(f))

if __name__ == '__main__':
	main()
