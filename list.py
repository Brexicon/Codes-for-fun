 



# StudentName = "Youself"

# StudentNames = ["Yousef","Shay","Brad"]

# print(StudentName)
# print(StudentNames[1])
# print(StudentNames[2])

# stNames = []
# stMarks = []

# numberOFStudents = int(input("How many students are in this class : "))

# for i in range (numberOFStudents) :
#     StName = input("Enter a students name # {0}\t :" .format(i+1))
#     StMark = input("Enter a students mark # {0}\t :" .format(i+1))
#     stNames.append(StName)
#     stMarks.append(StMark)

# print(stNames)
# print(stMarks)

stNames = []
stMarks = []

numberOFStudents = int(input("How many students are in this class : "))

for i in range (numberOFStudents) :
    StName = input("Enter a students name # {0}\t :" .format(i+1))
    StMark = float(input("Enter a {0}'s mark # {0}\t :" .format(StName)))
    stNames.append(StName)
    stMarks.append(StMark)

print(stNames)
print(stMarks)


# print("Failers are as follows")
# for i in range(numberOFStudents) :
#     if stMarks[i] < 60 :
#         print(stNames[i],stMarks[i])

# print("The students we helped are")
# for i in range(numberOFStudents) :
#     if stMarks[i] < 60 :
#         stMarks[i] = 60
#         print(stNames[i],stMarks[i])

# print("The total sum of all marks is " ,sum(stMarks))
# average = sum(stMarks) / len(stMarks)
# print("the average grade is : " , average)