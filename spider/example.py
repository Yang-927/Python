a = 666
b = 666
print("a-ID:", id(a))
print("b-ID:", id(b))
print(id(a))
if a == b:
	print("a等于b")
else:
	print("a不等于b")

if a is b:
	print("两者引用一个对象")
else:
	print("不是")

print(bin(927))
