#   A program to turn a quadratic in standard form to a quadratic in vertex form
#   John Paul Cannon
#   8 - 30 - 21

def quadToVert():
    
    #user input
    aVar = float(input("Enter your 'a' variable: "))
    bVar = float(input("Enter your 'b' variable: "))
    cVar = float(input("Enter your 'c' variable: "))

    #after factoring
    def solve():
        newCVar = (bVar / 2) ** 2
        subOutPar = -1 * aVar * newCVar
        totalOutPar = cVar + subOutPar


    
    
    if aVar != 1.0:
        print('gonna do this later')
    else:
        solve()

quadToVert()