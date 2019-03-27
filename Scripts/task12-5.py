from random_list import *
from iseven import *
def task():
	list=randomlist(10,10,0)
	idx=[]
	ls=[]
	for i in list:
		if iseven(i):
			ls.append(i)
			idx.append(list.index(i))
		else:
			continue
	return idx,ls,list
	#if len(ls) >= 2:
		


print(task())