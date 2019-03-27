def task105(s):
	x=0
	for i in s:
		if int(i) % 2 == 0:
			continue
		else:
			x=x+int(i)
	return x

s=str(input())
print (task105(s))