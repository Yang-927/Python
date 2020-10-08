import json

books = [
	{
		"name": "《 Hello World 》",
		"price": 88
	},{
		"name": "《JavaScript进阶》",
		"price": 99
	},{
		"name": "《Sublime Text》",
		"price": 66.8
	},{
		"name": "《PyCharm》",
		"price": 77.9
	}
]

# res = json.dumps(books, ensure_ascii=False);
# print(res)
# print(type(res))

with open('./books.json', 'r', encoding='utf-8') as f:
	# json.dump(books, f, ensure_ascii=False)
	print(json.load(f))


# json_str = '[{"name": "《 Hello World 》", "price": 88}, {"name": "《JavaScript进阶》", "price": 99}, {"name": "《Sublime Text》", "price": 66.8}, {"name": "《PyCharm》", "price": 77.9}]'
#
# result = json.loads(json_str)
# print(result)