from random_list import *
def task131():
    try:
            if iseven(int(input('Введите число: '))):
                    print('Четное')
            else:
                    print('Нечетное')
    except ValueError:
            print('Неверное значение аргумента')
    except KeyboardInterrupt:
            print('Программа прервана')



def task132():
	try:
		n=int(input('Высота '))
		m=int(input('Ширина '))
		for i in range(n):
			print (randomlist(m,10,0))
	except ValueError as e:
		print('Неправильный аргумент - "%s"') % e.args
		

task132()