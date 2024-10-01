




#input 
orderAmount = float(input("Enter your total order amount : "))

# Processing 

if orderAmount < 50 :
    totalBill = orderAmount + 10
else :
    totalBill = orderAmount
print("tour total bill is : {0:.2f} ". format(totalBill))
