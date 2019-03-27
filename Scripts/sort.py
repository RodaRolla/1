def printTop(stack):
	try:
		print (len(stack), stack[-1],sep='x')
	except: Exception
def multiplying(stack):
	stack.append(stack.pop()*stack.pop())

def addition(stack):
	stack.append(stack.pop()+stack.pop())

def subtraction(stack):
	stack.append(-stack.pop()+stack.pop())

def division(stack):
	try:
		stack.append((stack.pop()/stack.pop())**-1)
	except ZeroDivisionError:
		print('T_T')

stack=[]
queue=[]

func={
	'+': addition,
	'-': subtraction,
	'*': multiplying,
	'/': division
}




while True:
	for token in input().split(" "):
		try:
			if token == "stack":
				printTop (stack)
				printTop (queue)
			if token.isdigit:
				queue.append()
				continue
			if token in func:
				func[token](stack)
			if token == "(":
				stack.append()
				while token != ")":
					if token.isdigit:
						queue.append()
					if token in func:
						func[token](stack) 
			
		except (EOFError,Exception):
			print (len(stack))
			print (len(queue))