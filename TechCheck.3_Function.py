weeklySalary = float(input("Enter you weekly salary : "))

numOfDependents =float(input("Enter the number of dependents : "))


def taxWithheldCalculator() :


    provTaxAmount = .06 * weeklySalary

    fedTaxAmount = .25 * weeklySalary

    depnDeduction = .06 * weeklySalary * numOfDependents

    totalWithheld = provTaxAmount + fedTaxAmount - depnDeduction
    
    netSalary = weeklySalary - totalWithheld 

    print("The amount of federal tax withheld is ${0:.2f} " .format(fedTaxAmount))

    print("The amount of provincial tax withheld is ${0:.2f} " .format(provTaxAmount))

    print("The amount of tax deducted for dependts is ${0:.2f}" .format(depnDeduction ))

    print("The amount of tax withheld in tottal is ${0:.2f}" .format(totalWithheld))

    print("The amount of weekly take home is ${0:.2f}"  .format(netSalary))

    
taxWithheldCalculator()



print("My student Name is Bradley Horne")

print("MY student number is W0410733")