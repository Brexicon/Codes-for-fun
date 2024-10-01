




customerName = input("Enter Your name : ")
distanceForDelivery = float(input("Enter the distance : "))
costOfRecord = float(input("Enter the cost before tax : "))

deliveryCost = 15*distanceForDelivery
purchaseCost = costOfRecord * .014
totalCost = deliveryCost+purchaseCost
 

print("Old Mans Records and Other Old People stuff")

print("Purchase details for : ",customerName)
print("Purchase Cost is : {0:.2f}".format(purchaseCost))
print("Delivery Cost is : {0:.2f}".format(deliveryCost))
print("Purchase Cost is : {0:.2f}".format(totalCost))



