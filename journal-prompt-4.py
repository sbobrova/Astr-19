import numpy as np
import sys


class Panda:
	def __init__(self, arm_length, leg_length, numb_eyes, tail_yn, furry_yn):
		self.arm_length= 21.6
		self.leg_length= 20.3
		self.numb_eyes= 2
		self.tail_yn= True
		self.furry_yn= True
	def describe(self):
		print("My Panda's characteristics!")
		print(f"Their arms are {self.arm_length} in long.")
		print(f"Their legs are {self.leg_length} in long.")
		print(f"They have {self.numb_eyes} eyes.")
		print(f"Do they have a tail? {'Yes' if self.tail_yn else 'No'}!")
		print(f"Do they have fur? {'Yes' if self.furry_yn else 'No'}!")

def main():
	my_panda = Panda(arm_length=21.6, leg_length=20.3, numb_eyes=2, tail_yn=True, furry_yn=True)
	my_panda.describe()


if __name__=="__main__":
	main()



