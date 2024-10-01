


print("Old Mans Records and Other Old People stuff")
customerName=input("Enter Your name Please : ")
distanceForDelivery=float(input("Enter the distance, Please :"))
costOfRecord=float(input("Enter the cost before tax, Please :"))

deliveryCost=20*distanceForDelivery
purchaseCost=costOfRecord*1.15
totalCost=deliveryCost+purchaseCost

print("Purchase details for : ",customerName)
print("Purchase Cost is : {0:.4f}".format(purchaseCost))
print("Delivery Cost is : {0:.4f}".format(deliveryCost))
print("Purchase Cost is : {0:.4f}".format(totalCost))

