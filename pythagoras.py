import math

def pythagoras():
	a = float(input("Enter your 'a' value: "))
	b = float(input("Enter your 'b' value: "))
	c1 = a**2 + b**2 
	c = math.sqrt(c1)
	print("Your answer is: " + str(c) )