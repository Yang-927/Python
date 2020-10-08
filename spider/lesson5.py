# Xpath
from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('html/hello.html', parser=parser)

res = html.xpath('//li/@class')
print(res)
# for i in res:
# 	print(etree.tostring(i))


href = html.xpath('//li/a[@href="www.baidu.com"]')
print(href)
for i in href:
	print(etree.tostring(i))
# 	获取li下的span
span = html.xpath('//li//span')
for i in span:
	print(etree.tostring(i))

# 获取最后一个li里的a的href;

a = html.xpath("//li[last()]/a/@href")
print(a[0].text)
