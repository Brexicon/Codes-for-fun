
print("Customer order details")

print("Old Mans Records And Old People Stuff")


name = input("enter you name")
km = (input("enter dillivery disstance"))
totalRecords = (float(input("enter total cost of records")))

tax = 0.14 * totalRecords
dilliveryc = km * 15
purchesc = totalRecords + tax
total = purchesc + dilliveryc

print("the cumster is",name)
print("the total distance traveld",km)
print("the total cost of purches is",total)

print("summery for",name)
print("delivery cost",dilliveryc)
print("purches cost",purchesc)
print("total cost",total)