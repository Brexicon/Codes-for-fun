



studentNames = []
marksInPython = []
marksInDB = []

amountStudents = int(input("How many students do you have in this class : "))

for i in range (amountStudents):
    Names = input("What is this students name : ")
    pythonGrade = float(input("what did they get in the Python course : "))
    DBGrade = float(input("What did they get in the Date Base course : "))
    studentNames.append(Names)
    marksInPython.append(pythonGrade)
    marksInDB.append(DBGrade)


print("------------------------------------------------------------------")
print("Student Names \t Python Course \t Data Base Course")
print("------------------------------------------------------------------")
for i in range (len(studentNames)):
    print(studentNames[i], "\t\t", marksInPython[i],"\t\t", marksInDB[i]  )

totalInPython = sum(marksInPython)
totalInDB = sum(marksInDB)
print("The total mark in Python is", totalInPython, "and the total mark in Data Base is", totalInDB  )

pythonAverage = sum(marksInPython) / len(marksInPython)
DBAverage = sum(marksInDB) / len(marksInDB)
print("The average mark in python was", pythonAverage, "and the average mark in Data Base was", DBAverage)

print("--------------------First Report---------------------------------")

for i in range (len(studentNames)) :
    if marksInDB[i] < DBAverage :
        print(studentNames[i], "got a",marksInDB[i], "in the course Data Base" )

print("-------------Second Report--------------------------------------")

print("Students who we helped out in the Python Course")

for i in range (len(marksInPython)):
    if marksInPython[i] < 60 :
        marksInPython[i] = marksInPython[i] + 5
        print(studentNames[i], "got\t", marksInPython[i], "in Python Course")

for i in range (len(marksInDB)):
    if marksInDB[i] < 60 :
        print(studentNames[i], "failed the Data Base Course with a", marksInDB[i])

print("----------------------Third Report-------------------------------")

print("students Names before ascending order")

print(studentNames)

print("Students names after ascending order")

studentNames.sort()

print(studentNames)


