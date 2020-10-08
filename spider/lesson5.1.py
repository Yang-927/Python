import requests
from lxml import etree
import time

base_url = "https://www.guazi.com"
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4270.0 Safari/537.36",
	"cookie": "uuid=86c16db1-1450-4da3-eb9c-7f4a587f0357; ganji_uuid=3531807057899711627936; lg=1; close_finance_popup=2020-10-02; sessionid=5428abe4-8659-417f-9896-2c67b0800419; Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1601598510,1601599167; clueSourceCode=%2A%2300; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%2286c16db1-1450-4da3-eb9c-7f4a587f0357%22%2C%22ca_city%22%3A%22bj%22%2C%22sessionid%22%3A%225428abe4-8659-417f-9896-2c67b0800419%22%7D; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A34790349603%7D; user_city_id=26; preTime=%7B%22last%22%3A1601603735%2C%22this%22%3A1601598509%2C%22pre%22%3A1601598509%7D; cityDomain=sy; antipas=332ndP2Z44223241q7F432049; Hm_lpvt_936a6d5df3f3d309bda39e92da3dd52f=1601609152"
}

def get_detail_urls(buy_url):
	# 请求
	res = requests.get(buy_url, headers=headers)
	# urllib -> urlopen read() requests -> get/post text/content
	text = res.content.decode('utf-8')
	# 	将字节流转换成HTML
	html = etree.HTML(text)
	ul = html.xpath("//ul[@class = 'carlist clearfix js-top']")[0]
	lis = ul.xpath('./li')
	detail_urls = []
	for li in lis:
		detail_url = li.xpath('./a/@href')
		detail_url = base_url + detail_url[0]
		detail_urls.append(detail_url)
	return detail_urls

# 解析详情页
def parse_detail_url(detail_url):
		res = requests.get(detail_url, headers=headers)
		text = res.content.decode('utf-8')
		html = etree.HTML(text)
		name = html.xpath("//div[@class='product-textbox']/h2/text()")[0]
		info = html.xpath("//div[@class='product-textbox']/ul/li/span/text()")
		name = name.replace(r'\r\n', '').strip()
		mileage = info[2]
		displacement = info[3]
		gearbox = info[4]
		price = html.xpath("//div[@class='price-main']/span/text()")[0]
		infos = {}
		infos['name'] = name
		infos['mileage'] = mileage
		infos['displacement'] = displacement
		infos['gearbox'] = gearbox
		infos['price'] = price
		return infos
def main():
	buy_url = "https://www.guazi.com/bj/buy/"
	detail_urls = get_detail_urls(buy_url)

	for detail_url in detail_urls:
		infos = parse_detail_url(detail_url)
		# time.sleep(5)
		print(infos)

if __name__ == '__main__':
	main()
