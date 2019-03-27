def lib(a,b):
	dict={}
	if len(a)==len(b):
		for x in range(0,len(a)):
			if x % 2 == 0:
				dict.update({b[x]:a[x]})
			else:
				dict.update({a[x]:b[x]})
		return dict
	else:	
		raise Exception('количество элементов в списках не равны')
def replace():
	pass


if __name__=='__main__':
	a_list=['qaz','wsx','edc','rfv']
	b_list=["123","345","789","012"]
	try:
		print(lib(a_list,b_list))
	except Exception as e:
		print (str(e))