import math
def geron(a,b,c):
	p=eval('(a+b+c)/2')
	s=math.sqrt(eval('(p*(p-a)*(p-b)*(p-c))'))
	
	return s

a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))

print(geron(a,b,c))