import numpy as np
import sys

def main():
	w= 3.9 #float
	x= 4.6 #float
	y= 7   #integer
	z= 2   #integer

	float_sums = w+x

	print("The floats are:",w,"and",x)
	print("The integers are:",y,"and",z)

	print("The sum of the floats is:", float_sums)
	print("Type:", type(float_sums))

	int_diff = y-z

	print("The difference between the integers is:", int_diff)
	print("Type:", type(int_diff))

	num_prod = w*y

	print("The product of an integer and a float is:", num_prod)
	print("Type:", type(num_prod))

if __name__=="__main__":
	main()
