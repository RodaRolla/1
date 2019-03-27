import random

x=random.randint(1,6)
y=random.randint(1,6)
print ("первый игрок выбросил %s" % x)
print ("второй игрок выбросил %s\n" % y)
if x>y:
	print('%s больше' % x)
elif x<y:
	print('%s больше' % y)
else:
	print ('оба равны')