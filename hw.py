x=int(input("Enter fizz:"))
y=int(input("Enter buzz:"))
z=int(input("Enter the number:"))
for i in range(1,z+1):
	if  not i%x:
		print('F', end="")
	elif not i%y:
		print("B",  end="")
	elif not i%x and not i%y:
	   print("FB",  end="" )
	else:
		print(i,  end="" )
print(i)

















