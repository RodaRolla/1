def prime_num(n):
	lst=[]
	k=0
	for i in range(2,n+1):
		for j in range(2,i):
				if i%j==0:
					k+=1
		if k == 0:
				lst.append(i)
		else:
				k=0
	return lst


#n=int(input('n= '))
#print(prime_num(n))