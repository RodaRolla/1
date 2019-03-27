def printTop(stack):
	try:
		print (len(stack), stack[-1],sep='x')
	except: Exception
def multiplying(stack):
	stack.append(stack.pop()*stack.pop())

def addition():
	right=numStack.pop()
	left=numStack.pop()
	numStack.append(left+right)
	print("Add %d+%d=%d" % (left,right,numStack[-1]))

def subtraction():
	right=numStack.pop()
	left=numStack.pop()
	numStack.append(left-right)
	print("Sub %d-%d=%d" % (left,right,numStack[-1]))

def division(stack):
	try:
		stack.append((stack.pop()/stack.pop())**-1)
	except ZeroDivisionError:
		print('T_T')	
func={
	'+': addition,
	'-': subtraction,
	'*': multiplying,
	'/': division
}
	
def isNumber(ls):
	for c in ls:
		if c not in '0123456789.':
			break
	else:
		return True
	return False
	 
def isFunc(ls):
	if ''.join(ls) in func:
		return True
	return False
	
def isSame(a,b):
	if a == []:
		return False	# bug!
	if isNumber(a):
		if isNumber(b):
			return True
		return False
	if isFunc(a):
		if isFunc(b):
			return True
		return False
		
# или число или фнкция
def parseTokens(ls):
	out=[]
	tk=[]
	for symbol in ls:
		print("symbol=%s" % symbol)
		if isSame(tk,symbol):
			tk.append(symbol)
			print("Same! symbol '%s' -> %s" % (symbol,tk))
		else:
			if tk!=[]:
				out.append(''.join(tk))
				print("Out=%s" % out)
			tk=[symbol]
			print("Symbol '%s' => %s" % (symbol,tk))
	if tk!=[]:
		out.append(''.join(tk))
	print(out)
	return out
		
def infixToPostfix(ls):
	stack=[]
	out=[]
	
	for token in ls:
		if isNumber(token):
			out.append(int(token))
			print(out)
		if isFunc(token):
			if stack==[]:
				stack.append(token)
			else:
				out.append(stack.pop())
				stack.append(token)
			#if token == '+':
			#	out.append(out.pop()_int+out.pop())
		
		# число -> в аут
		# оператор - в стек
	# из стека операторы в ат
	for op in stack[::-1]:
		out.append(op)
	print("Postfix=%s" % out)
	return out

def doToken(token):
	if isinstance(token,int):
		numStack.append(token)
	else:
		if token in func:
			func[token]()
		else:
			print("Syntax error with '%s'" % token) # throw exeption!

#while True:
	#numStack=[]
#	for token in infixToPostfix(parseTokens(input())):
	#	print(token)
	#	doToken(token)
#	print("Result=%s" % numStack)
def cycle(infixToPostfix,parsTokens,token,ls):	
	while True:
		numStack=[]
		for token in infixToPostfix(parsTokens(input())):
			print(token)
			doToken(token)
		print ("Result=%s" % numStack)







