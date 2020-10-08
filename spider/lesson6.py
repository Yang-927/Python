from bs4 import BeautifulSoup
from lxml import etree
axml='''
	<body>
	   <div>
		  <ul>
			 <li class="item-0">< a href=" ">first item</ a></li>
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
print(soup.li.name)