




VarOne = 10 #Global variable

def printValue() :
    varTwo = 20 #varTwo is a local variable
    varThree = 30 #varThree is a local variable
    print(varTwo)
    VarOne = 15 #I am declaring a new local variable 
    print(varThree)
    print(VarOne)
    print(VarFour)
    return

VarFour = 100
printValue() #Calling the function printValue()
print(VarOne) #Printing Global variable#vartwo is a local variable


