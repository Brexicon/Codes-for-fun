# this is my name: Brad Horne
# this is my Student Number: W0410733


#what input do i need
#dose it need to be float, string or int 

#input

dataUsage = float(input("Enter your date usage for the month please : "))

#what are my if statements and how do i want to write them
#what math do i need it do 

#proces

if dataUsage <= 200 :
    dataBill =  20 
if dataUsage >= 200 or dataUsage < 500 :
    monthyBill = .105
if dataUsage >= 500 or dataUsage < 1000 :
    monthyBill = .11
if dataUsage >= 1000 :
    monthyBill = 180

dataBill = dataUsage * monthyBill

#how will i print this statement 

#output

print("Your monthy bill is : {0:.2f} " .format(dataBill) )