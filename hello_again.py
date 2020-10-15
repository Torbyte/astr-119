def main():
	i = 0 # integer of i = 0
	x = 119.0 # x = 119.0

	for i in range(120): 

		if( (i%2)==0 ): #
			x += 3.0
		else:
			x-= 5.0

	s = "The value of x is x = %3.2e" % x
	print(s)


if __name__ == "__main__":

	main()