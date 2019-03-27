l = [3,6,7,4,-5,4,3,-1]
def taskOne():
	if sum(l) > 2:
		print(len(l))


def taskTwo():
	if abs(min(l) - max(l)) > 10:
		print(sorted(l))
	else:
		print('<10')

taskTwo()