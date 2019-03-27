import urllib.request
def urltask():
	open('example.txt','w',encoding='utf-8').close()
	url = 'http://dfedorov.spb.ru/python/files/tutchev.txt'
	with urllib.request.urlopen(url) as webpage:
		for line in webpage:
			f=open('example.txt','a',encoding='utf-8')
			f.write(str(line.decode('utf-8')))
			f.close()
	

urltask()
