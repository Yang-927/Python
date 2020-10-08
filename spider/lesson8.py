import re
# str = 'abc'
# res = re.match('a', str)
# print(res.group())

# str = "*sdadasf65456415dfa8g"
# res = re.search('\w+?', str)
# print(res.group())

# html = "<td>Hello World</td>"
# res = re.search('<.+?>', html)
# print(res.group())

# str = '00001'
# res = re.search("0$|[1-9]\d?$|100$", str)
# print(res.group())

text = "Apple price is $65,banana price is $87"
res = re.search('.+(\$\d+).+(\$\d+)', text)
print(res.groups())

tel = '17810699974'
res = re.search('0?(13|14|15|17|18|19)[0-9]{9}', tel)
print(res.group())

idCard = "410521199912308013"
res = re.search('\d{17}[\d|x]|\d{15}', idCard)
print(res.group())