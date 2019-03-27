def isint(value):
	if (value/2).is_integer():
		return ("%s - четное" % value)
	else: 
		return ("%s - нечетное" % value)

try:
	print(isint(float(input('Введите число: '))))
except ValueError:
	print ('это не является числом')