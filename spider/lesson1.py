from bs4 import BeautifulSoup
axml = '''
	<settings>
		<dd key="d1" value="1">
		<dd key="d2" value="2">
		<dd key="d3" value="3">
		<dd key="d4" value="4">
	</settings>
'''

soup = BeautifulSoup(axml, 'lxml')

for s in soup.findAll('dd', {'key': 'd2'}):
	print(s.get('value'))
