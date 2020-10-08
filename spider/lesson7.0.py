from bs4 import BeautifulSoup
from lxml import etree
axml='''
	<body>
	   <div>
		  <ul>
			 <li class="item-0" age="22" weight="67">< a href=" ">first item</ a></li>
			 <li class="item-1">< a href="link2.html">second item</ a></li>
			 <li class="item-inactive">< a href="link3.html"><span class="bold">third item</span></ a></li>
			 <li class="item-1">< a href="link4.html">fourth item</ a></li>
			 <li class="item-0">< a href="link5.html">fifth item</ a>
		  </ul>
	   </div>
	   <b><!-- 我是一行注释 --></b>
	</body>
'''
soup = BeautifulSoup(axml, 'lxml')
# print(soup.li)
print(soup.li.name)				# 获取标签的名称
print(soup.li.attrs)			# 获取标签里的属性，所有属性
print(soup.li["class"])			# 获取标签的class属性
print(soup.li.get('class'))		# 获取标签的class属性

print(soup.li.string)			# 获取标签中的内容
print(type(soup.li.string))		# 获取类型
print(type(soup))

print(soup.b.string)
print(type(soup.b.string))

