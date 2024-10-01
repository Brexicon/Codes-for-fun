




weeklySalary = float(input("Enter you weekly salary : "))

numOfDependents =float(input("Enter the number of dependents : "))


def taxWithheldCalculator() :


    provTaxAmount = .06 * weeklySalary

    fedTaxAmount = .25 * weeklySalary

    depnDeduction = .06 * weeklySalary * numOfDependents

    totalWithheld = provTaxAmount + fedTaxAmount - depnDeduction
    
    netSalary = weeklySalary - totalWithheld 

    print("The amount of federal tax withheld is " , fedTaxAmount)

    print("The amount of provincial tax withheld is " , provTaxAmount )

    print("The amount of tax deducted for dependts is" , depnDeduction )

    print("The amount of tax withheld in tottal is " , totalWithheld)

    print("The amount of weekly take home is " , netSalary)

    
taxWithheldCalculator()
        
taxWithheldCalculator()


print("My student Name is Bradley Horne")

print("MY student number is W0410733")