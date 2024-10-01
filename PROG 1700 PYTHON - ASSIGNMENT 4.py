




daysWorked =[1,2,3,4,5]
hoursWorked = []

for i in range (len(daysWorked)) : 
    hoursPreDay = float(input("How long did you work on day {0}? \t " .format(daysWorked[i])))

    hoursWorked.append(hoursPreDay)

print (hoursWorked)

longestDayWorked = 0
maxDays = 0
for i in range (len(hoursWorked)):
    if longestDayWorked < hoursWorked[i]:
        longestDayWorked = hoursWorked[i]
        maxDays = daysWorked[i]

print("The most hours worked was on day", maxDays, "For a total of", longestDayWorked)

sumOfHoursWorked = sum(hoursWorked)
print("The toatal mount of hours worked this week was\t", sumOfHoursWorked)

averageHours = sumOfHoursWorked / len(hoursWorked)
print("The average amount of hours worked was" ,averageHours)

for i in range (len(daysWorked)): 
    if hoursWorked[i] < 7 :
        print("You were a slacker on day", daysWorked[i], "with a total hours worked of", hoursWorked[i] )


print("Student name - Bradley R Horne")
print("Student number - W0410733")