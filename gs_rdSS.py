import random
x = 0
y = 1
z = 100
r = random.randint(1, 100)
while True:
	x = x + 1
	num = random.randint(y, z)
	print('答案是: ', num)
	if num == r:
		print('猜對了，你猜了', x, '次')
		break
	elif num < r:
		print('再大一點，你猜了', x, '次')
		y = num + 1
	else:
		print('小一點拉~~~，你猜了', x, '次')
		z = num - 1