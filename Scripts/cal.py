#!/usr/bin/python
## -*- coding: utf-8 -*-

def printTop(st):
	try:
		print "[%d] %d" % (len(st), st[-1])
	except Exception:
		print "Ой-ой! Стек пустой!"

def sAdd(st):
	st.append(stack.pop()+stack.pop())

def sSub(st):
	st.append(-stack.pop()+stack.pop())

def sMul(st):
	st.append(stack.pop()*stack.pop())

def sDiv(st):
	x=st.pop()
	y=st.pop()
	st.append(y/x)

def sRem(st):
	x=st.pop()
	y=st.pop()
	stack.append(y%x)

def sPop(st):
	st.pop()

def sDup(st):
	x=st.pop()
	st.append(x)
	st.append(x)

ops={
	'+': sAdd,
	'-': sSub,
	'*': sMul,
	'/': sDiv,
	'%': sRem,

	'^': sPop,
	'd': sDup
}

stack=[]
try:
	while True:
		print "Пиши код: "
		for token in raw_input().split(' '):
			#print "Токен='%s'" % token
			try:
				if token == 'exit':
					#print "взять из стека ответ, вывести и выйти"
					printTop(stack)
					exit(0)
				if token.isdigit():
					#print "положить %s в стек"  % token
					stack.append(int(token))
					printTop(stack)
					continue
				if token in ops:
					ops[token](stack)
					printTop(stack)
				else:
					print "Не знаю, что делать с '%s'" % token
			except IndexError:
				print "Нарушен синтаксис, стек кончился :("
		#print "вывести глубину и вершину стека"
		#printTop(stack)
		print "Стек = %s" % stack
except (KeyboardInterrupt,EOFError):
	print "всего хорошего!"
	exit(0)

