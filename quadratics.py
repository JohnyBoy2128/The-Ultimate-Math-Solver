#    Program to solve quadratic formulas from standard form
#    John Paul Cannon
#    8 - 29 - 21

import math
import cmath
import PySimpleGUI as win

window = win.Window("Demo")

def quadratics():
	aVar = float(input("Enter your 'a' value: "))
	bVar = float(input("Enter your 'b' value: "))
	cVar = float(input("Enter your 'c' value: "))

	#doing basic variable calculations
	twoAVar = 2 * aVar
	negBVar = -1 * bVar
	bVarSquared = bVar * bVar
	insideRadical = bVarSquared - (4 * aVar * cVar)

	#functions to do math
	def nonImagAnsw(twoAVar, negBVar, insideRadical):
		print("The possible answers are: ")
		print("\tx = " + str((negBVar + math.sqrt(insideRadical)) / twoAVar))
		print("\tx = " + str((negBVar - math.sqrt(insideRadical)) / twoAVar))
	
	def imagAnsw(twoAVar, negBVar, insideRadical):
		print("The possible answers are: ")
		print("\tx = " + str((negBVar + cmath.sqrt(insideRadical)) / twoAVar))
		print("\tx = " + str((negBVar - cmath.sqrt(insideRadical)) / twoAVar))

	#conditional for whether real or imaginary
	if (bVarSquared - (4 * aVar * cVar) >= 0):
	  nonImagAnsw(twoAVar, negBVar, insideRadical)
	else:
		imagAnsw(twoAVar, negBVar, insideRadical)