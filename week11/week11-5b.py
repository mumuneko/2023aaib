a,b=list(map(int,input().split()))
if a>b:
	a,b=b,a #be careful! Who is small
for i in range(a,b+1):#change a and b
	if i%5==0:print(i)