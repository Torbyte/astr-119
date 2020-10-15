try:
	print(a) #this will throw an exception
except:
	print("a is not defined")
#specific types of error
try:
	print(a)
except NameError:
	print("a is still not defined")
except:
	print("Something else went wrong.")
print(a)