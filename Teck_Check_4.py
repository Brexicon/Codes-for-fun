
print("Grade point Calculator")
print("Valid letter grades that can be entered: A, B, C, D, F.") 
print("Valid grade modifiers are +, - or nothing. ")
print("All letter grades except F can include a + or - symbol." )
print("Calculated grade point value cannot exceed 4.0." )

 
letterGrade = input("Enter a letter grade for student : ")
modGrade = input("Enter a grade modifire +,- or nothing")
numValue = 0



if letterGrade.upper() == "A": 
    numValue = int(4) 

elif letterGrade.upper() == "B": 
    numValue = int(3) 

elif letterGrade.upper() == "C": 
    numValue = int(2)

elif letterGrade.upper() == 'D': 
    numValue = int(1) 

elif letterGrade.upper() == "F": 
    numValue = int(0) 




if modGrade == "+" :
    numValue = numValue + .3

elif modGrade == "-" :
    numValue = numValue - 0.3

else :
    numValue = numValue  

# as long as the grade is less then .5 it is 0(could have used .4, just like .5 more)
if numValue < .5 :
    numValue = 0
# as long as grade is over 4 it is 4
if numValue > 4 :
    numValue = 4

else :
    numValue = numValue


print("Your finle grade for the course will be", numValue)
    

print("Student name Bradley R Horne")
print("Student number W0410733")
