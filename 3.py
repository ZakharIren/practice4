y=int(input("Enter the number"))

for i in range(1,y//2+1):
	if not y%i:
		print(i, end=" ")
print(y)

