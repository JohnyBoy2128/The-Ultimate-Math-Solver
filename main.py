#   A program to solve many types of mathematical problems
#   Elijah James & John Paul Cannon
#   Started 8 - 27 - 21
#   EJC

#imported functions
import quadratics
import pythagoras
import circumfrence
import PySimpleGUI as win

#window layout for pysimplegui
layout = [
  [win.Text("Welcome to The Ultimate Math Problem Solver")],
  [win.Text("Choose what type of math problem you want solved")],
  [win.Button("Quadratic Equation")], 
  [win.Button("Pythagorean Theorum")],
  [win.Button("Circumference of a Circle")]
]

#create the window
window = win.Window("Demo", layout)

#create an event loop
while True:
    event, values = window.read()
    
    #conditional for what user chose
    if event == "Quadratic Equation":
      window.close()
      quadratics.quadratics()
    elif event == "Pythagorean Theorum":
      window.close()
      pythagoras.pythagoras()
  
window.close()


print("Welcome to The Ultimate Math Problem Solver!")
print("Choose the type of math problem you are trying to solve.")
print("")
print("\t1. Quadratic Equation")
print("\t2. Pythagorean Theorum")
print("\t3. Circumference of a Circle")
userInput = int(input())

if userInput == 1:
	quadratics.quadratics() 
elif userInput == 2:
	pythagoras.pythagoras()
elif userInput == 3:
	circumfrence.circumfrence()


