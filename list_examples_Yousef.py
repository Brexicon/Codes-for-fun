



stNames =["Yousef", "Brad", "Geoff"]

stGrades = [78, 95, 100]

# print(stNames)
# print(stGrades)

#if index out of range (the loop is to high) it will not run

for i in range(3) :
    print(stNames[i])

for i in range(3) :
    print(stGrades[i]) 

print("Total elements in stNames list : " , len(stNames))

for i in range(len(stNames)) :
    print(stNames[i])

print("stNames     stGrades")
print("--------------------")
for i in range(len(stNames)) :
    print(stNames[i], " " ,stGrades[i])


#foreach loop : ussaly used with a list

for stName in stNames:
    print(stName)
for stGrade in stGrades:
    print(stGrade)


    
##############################################################################


stNames =["Yousef", "Brad", "Geoff"]

stGrades = [78, 95, 100, -10000, 34, 101]


stNames.append("eli")
stGrades.append(82)
stNames.append("Geoof")
print (stNames)
print (stGrades)
stNames.remove(stNames[4])
print(stNames)

stNames.insert(1, "BadName")
print(stNames)
for i in range(len(stNames)):
    print(stNames[i])

for i in range(len(stNames)):
    if stNames[i] == "Yousef" :
        stNames[i] = "Yousef The Best"

for i in range(len(stNames)):
    print(stNames[i])

for i in range(len(stGrades)) :
    if stGrades[i] < 0:
        stGrades[i] = 0
    if stGrades[i] > 100 :
        stGrades[i] = 100
for i in range(len(stGrades)) :
    print(stGrades[i])



##################################################################################################################

# stNames = [] 

# i = 0

# while (i < 10) :
#     stNames.append(input("Enter student name : "))

#     i += 1

# print(stNames)

# for q in range(len(stNames)) :
#     print(stNames[q])