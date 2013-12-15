def isSushu(x):
    for i in range(2,x/2+1):
	if x%i == 0:
	    return False
    else:
	return True

a = [x for x in range(2,100) if isSushu(x)]
for x in a:
   print x
