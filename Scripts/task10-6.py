def task106():
	while True:
		x=0
		for token in input().split(' '):
			try:
				if token.isdigit:
					x=x+int(token)
				elif token == 'Стоп':
					return False
				else:
					continue
			except Exception:
				return ('heh')
		return x

print(task106())