x = int(input("Enter the number"))
if (x%2 and not x%3 and not x%5 and x%10):
	print(x)
else:
	print("Nothing")