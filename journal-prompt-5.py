import numpy as np
import sys

def main():
	x_values= np.linspace(0,2*np.pi,1000)

	print(f'{'x':>10}{'sin(x):>10'}')
	print("-"*22)

	for x in x_values:
		sin_x = np.sin(x)
		print(f"{x:10.6f}{sin_x:10.6f}")

if __name__=="__main__":
	main()