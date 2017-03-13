def decr_num(num):
	if num >= 1:
		print num
		num = num - 1
		decr_num(num)


decr_num(100)
