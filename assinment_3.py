# this is my name: Brad Horne
# this is my Student Number: W0410733

#first what are my variables and what will i call them
#what needs to be forced to be float, string or in
#input

houseNum = input("Please eneter you house number : ")

treeAmount = int(input(" enter your tree amount : " ))

grassType = input("enter you grass type : ")

propertyDeth = float(input("enter the depth of the yard : "))

propertyWidth = float(input("enter ther width "))

baseLabour = float(1000)

#what do i need to do for math and format of it 
#how will i write my if statement and what will i use (if, else or elif)

#process
treeCost = treeAmount * 100

lawnSize = propertyDeth * propertyWidth

if lawnSize > 5000 :
    baseLabour = baseLabour + 500 
else  :
    baseLabour = 1000

if grassType.lower() == "fescue" :
    grassCost = float(0.05)
elif grassType.lower() == "bentgrass" :
    grassCost = float(0.02) 
elif grassType.lower() == "campus" :
    grassCost = float(0.01)

finalCost = (lawnSize * grassCost) + treeCost + baseLabour


#how i will my print statement look

#output


print("For house {0} your amount is : ${1:.2f} "  .format(houseNum, finalCost ))