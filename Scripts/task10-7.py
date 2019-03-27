import re
def das():
	s="Мой дядя самых честных правил, Когда не в шутку занемог, Он уважать себя заставил И лучше выдумать не мог"
	#'\s*(\w+)\s*=\s*([^#]*?)\s*(#.*)?$'
	result = re.findall('[Мм]\w+',s)
	print(result)

def task():
	list=[]
	s=input().split(' ')
	for i in s:
		list.append(len(i))
	return print(max(list))		

task()