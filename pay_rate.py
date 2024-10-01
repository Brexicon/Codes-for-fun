print("Weekly Payment Calculator Prigram")


iverTimeHours = 0
actualWorkingHours = 0
hourlyPayRate = 0.0
fixedWeeklyHours = 40

actualWorkingHours = int(input("Enter your hours worked this week : "))
hourlyPayRate = float(input("ENter the hourly rate : "))


#procesing



if actualWorkingHours > 40 :
    overTimeHours = actualWorkingHours - fixedWeeklyHours
    overTimePayment = overTimeHours * hourlyPayRate * 1.5
    totalWeeklyPayment = hourlyPayRate * fixedWeeklyHours + overTimeHours

else actualWorkingHours < 40 
    
        

print ("Your weekly Payment is : $ {0:.2f}" , format(o)(totalWeeklyPayment))