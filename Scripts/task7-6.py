import math
def fnuc(x):
	if x*100 in range(20, 90):
		f=math.sin(x)
	else:
		f=1
	return f
	
if __name__=="__main__":
	print(fnuc(input()))