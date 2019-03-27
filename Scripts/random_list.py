import random

def randomlist(n,upedge,lowedge):
	list=[]
	for i in range(0,n):
		list.append(random.randint(lowedge,upedge))
	return list