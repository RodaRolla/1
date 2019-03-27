
def task9five(x,y):
	list=[]
	list.append(x)
	list.append(y)
	if (x+y).isdigit():
		list.append(str(int(x)+int(y)))
		list[1],list[2] = list[2],list[1] 
	else:
		list.append(x+y)
	return list
		
x=input()
y=input()


print(task9five(x,y))