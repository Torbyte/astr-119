import numpy as np
import sys

#define a function that returns a value

def expo(x):
	return np.exp(x)
#define a subroutine that doesn't return a variable
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))

#define a main function
	def main():
	n = 10
	#check if there is a main line argument
	if(len(sys.argv)>1):
		n = int(sys.argv[1]) # set n to 2nd command
	show_expo(n) #show the show_expo route

	print("the value of n is ",n)
	print('the value of argv is',sys.argv)
if __name__ == "__main__":
	main()