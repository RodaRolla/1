import random
n=int(input('Размер матрицы '))
#m=int(input('высота: '))
x=0
for q,w in enumerate([[random.randint(-10,10) for x in range(n)] for y in range(n)]):
	print(w)
	x=x+w[q]
	
		
print('diag= ',x)
