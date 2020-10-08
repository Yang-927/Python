from bs4 import BeautifulSoup
axml = '''
	<settings>
		<dd key = "d1" value = "1">
		<dd key = "d2" value = "2">
		<dd key = "d3" value = "3">
	</settings>
'''

soup = BeautifulSoup(axml, 'lxml')
dd_list = soup.findAll('dd', {'key': 'd1'})

# print(type(dd_list))
# for 变量 in 列表、字典、元组、集合:
# for s in dd_list:
# 	print(s.get())

for Curry in dd_list:
	print(Curry.get("value"))
