from bs4 import BeautifulSoup
from lxml import etree

path = "C:/Users/YANG/Desktop/Python/spider/html/Yang.html"
htmlfile = open(path, 'r', encoding='utf-8')
html = htmlfile.read()
soup = BeautifulSoup(html, 'lxml')

trs = soup.find_all('tr')
# print(trs)

# tr = soup.find_all('tr', limit=2)[1]

# tr = soup.find_all('tr', class_='even')
# print(tr)

# a = soup.find_all('a')
# print(a)

# for i in a:
# 	print(i.attrs['href'])

trs = soup.find_all('tr')[1:]
for i in trs:
	td = i.find_all('td')[0]
	print(td.get_text())
