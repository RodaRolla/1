m=['вася','петя','женя','коля','саша','жора']
f=['надя','маша','саша','света','женя','настя','гертруда']
l=m+f
def nomatch(list):
	for i in list:
		while list.count(i) > 1:
			list.remove(i)
	return list


def Two1():
	matchList=[]
	for i in f:
		if i in m:
			matchList.append(i)
		else:
			continue
	return matchList

def Two2():
	m2=['вася','петя','женя','коля','саша','жора']
	f2=['надя','маша','саша','света','женя','настя','гертруда']
	l=set(m+f)
	for i in l:
		if i in Two1():
			m2.remove(i)
			f2.remove(i)		
		else:
			continue
	return print ('не повторяющиеся мужские: \n',m),print ('не повторяющиеся женские: \n',f)


print('Повторяются: \n',Two1())
Two2()
print ('Список все имен: \n',nomatch(l))
print(m,f)