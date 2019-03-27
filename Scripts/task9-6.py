import random
def task9Six(list):
	x=random.choice(list)
	l=random.choice(x)
	m=x.replace(l,'?')
	return list,x,l,m
	
#import random
#list= ['самовар', 'весна', 'лето']
#print (list)
#print(random.choice(list))
#print(random.choice(random.choice(list)))
if __name__=='__main__':
	list= ['самовар', 'весна', 'лето']
	print (task9Six(list))