import random

r = random.randint(1, 100)
while True:
	num = input('1到100猜猜看: ')
	num = int(num)
	if num == r:
		print('猜對了')
		break
	elif num < r:
		print('再大一點')
	else:
		print('小一點拉~~~')
