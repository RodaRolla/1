import random
def task(n):
		
	string=''
	for i in range(n):
		string=string+str(random.randint(0,9))
	#list.append(string[int(len(string)/2):])
#	list.append(string[:int(len(string)/2)])
	s=string[:int(len(string)/2)]+' and '+string[int(len(string)/2):]
	return string,s
print (task(int(input())))