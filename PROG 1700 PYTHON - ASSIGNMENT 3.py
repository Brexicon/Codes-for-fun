




"Program 1: FirstLoop"
 
#Write a while loop statement that print:

# A- All positive numbers that are divisible by 10 and less than n. For example, if n is 100, print 10 20 30 40 50 60 70 80 90.
#  Note: Use a function called printPositiveNumbers to perform this loop by passing the value of n.
# 																(2.5 marks)

"""
n = int(input("Enter a number of your chose : "))
c= 1
def printPositiveNumbers (n,c):

    while c < n :
        if c % 10 == 0 :
            print(c)
        c += 1

printPositiveNumbers(n,c)
"""


# B- All powers of two less than n. For example, if n is 100, print 1 2 4 8 16 32 64.
# 	Note: Use a function called printPowersOfTwo to perform this loop by passing the value of n.

"""
nTwo = int(input("ENter a number of your chose : "))
cTwo = 0

def printPowersOfTwo(nTwo,cTwo) :

    while 2 ** cTwo <= nTwo :
        print (2 ** cTwo)
        cTwo += 1
    
printPowersOfTwo(nTwo, cTwo)
"""

 #"""Program 2: SecondLoop"""

# Write a loop statement that computes:

# A- The sum of all even numbers between 2 and 200 (inclusive). 
# Note: Use function called sumOfEvenNumbers to perform this loop.
# (2.5 marks)

"""
nThree = 2
s = 0

def sumOfEvenNumbers(nThree,s) :

    while nThree < 200 +1 :
        if ((nThree % 2) == 0) :
            s = s + nThree
        
        nThree += 1

    print ("The sum of all even numbers are" ,s )

sumOfEvenNumbers(nThree,s)
"""

# B- The sum of all squares between 1 and 200 (inclusive). Use function called sumOfSquares to perform this loop.

"""
sumOf = 0

def sumOfSquares(sumOf):

    for i in range (1, 200 + 1):
        sumOf = sumOf + (i * i) 
    
    print("The sum of all squares are" ,sumOf)

sumOfSquares(sumOf)
"""

# ----- Program 3: ThirdLoop

# Write program that read a sequence of integer inputs and print:

# A- The smallest and largest of the inputs.	

"""
numOfint = int(input("Enter the amount of numbers you would like to input : "))
numL = int(input("Enter your first number : "))
numS = int(input("ENter your Second number : "))
numC = int(input("Enter a number to compare : "))
count = 0

while count < numOfint :

    if numL < numC :
        numL = numC
    else :
        numL = numL

    if numS > numC :
        numS = numC
    else :
        numS = numS

    numC = int(input("Enter a new compare number : "))
    count += 1

print("The largest number is", numL)
print("The smallest number is ", numS)
"""

# B- The number of even inputs.

"""
numOfint = int(input("Enter the amount of numbers you would like to input : "))
numE = int(input("Enter a random number here : "))
count = 0 
countE = 0
countO= 0
while count < numOfint :

    if numE % 2 ==0 :
        countE += 1
    else :
        countO += 1

    numE = int(input("ENter a new number : "))
    count += 1

print("The number of even nubers are " ,countE)
print("The number of odd numbers are " ,countO)
"""

print("Student name Bradley R Horne")
print("Student number W0410733")