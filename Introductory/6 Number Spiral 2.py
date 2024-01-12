for i in range(int(input())) :
	x,y=map(int,input().split())
	if x<y :
		if y%2==1 :
			print((y*y)-(x-1))
		else :
			print(((y-1)*(y-1))+x)
	elif x==y :
		if y%2==1 :
			print((y*y)-(x-1))
		else :
			print((x*x)-(y-1))
	else :
		if x%2==0 :
			print((x*x)-(y-1))
		else :
			print((x-1)*(x-1)+y)
