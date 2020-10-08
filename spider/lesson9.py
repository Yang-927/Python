# import csv
#
# header = ('姓名','年龄','身高')
# stus = [
# 	('Curry', 32, 191),
# 	('Durant', 32, 210),
# 	('Kobe', 35, 195)
# ]

# with open('stus.csv', 'w', encoding='utf-8', newline='') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(header)
# 	writer.writerows(stus)

# import csv
#
# header = ('name', 'age', 'height')
# stus = [
# 	{'name': 'Curry', 'age': 32, 'height': 191},
# 	{'name': 'Durant', 'age': 32, 'height': 210},
# 	{'name': 'Kobe', 'age': 35, 'height': 195}
# ]
#
# with open("stus.csv", "w", encoding="utf_8_sig",newline='') as f:
# 	wd = csv.DictWriter(f, header)
# 	wd.writeheader()
# 	wd.writerows(stus)

# reader
import csv

with open('stock.csv', 'r', encoding='gbk') as f:
	reader = csv.DictReader(f)
	for i in reader:
		print(i['secShortName'])
		print(i)