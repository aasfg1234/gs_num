import random
x = 0
start = input('最小多少: ')
end = input('最大多少: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
while True:
	x = x + 1
	num = random.randint(start, end)
	print('答案是: ', num)
	if num == r:
		print('猜對了，你猜了', x, '次')
		break
	elif num < r:
		print('再大一點，你猜了', x, '次')
		start = num + 1
	else:
		print('小一點拉~~~，你猜了', x, '次')
		end = num - 1