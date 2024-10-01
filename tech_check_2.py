




sudentName = (input("enter sudent name : " ))
courseName = (input("Enter Course name : "))
absences = float(input("NUmber of classes missed : "))
atendances = float(input("Number of classes atendead : "))

totalDay = atendances + absences
atenPercent = atendances / totalDay * 100

print("The students name is ", sudentName)
print ("The Course name is ",  courseName )



print("The ADendances precentage is{0:.2f} ". format (atendances))