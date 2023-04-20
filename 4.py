x = int(input("Enter the number"))
s=0
while x:
	a=x%10
	x=x//10
	print (a,' *10^', s )
	s+=1