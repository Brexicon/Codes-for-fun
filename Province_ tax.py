'''student name and number - Bradley R Horne, W0410733
'''




counrtyName = input("Enter the counrty name : ")

totalOrder = float(input("wWhat is the total order? :"))


def CountryCanada(counrtyName):


    if counrtyName.lower() == "canada" :
        provinceName = input("Enter province name : ")

        if provinceName.lower() == "alberta" :
            taxAmount = 0.05 * totalOrder

        elif provinceName.lower()  == "ontario" or provinceName.lower() == "nova scotia" or provinceName.lower() == "new brunswick" :
            taxAmount = 0.15 * totalOrder

        else :
            taxAmount = 0.11 * totalOrder        

    finalTotal = totalOrder + taxAmount
    print("Your total with tax is {0:.2f} " .format( finalTotal )) 

    return

def otherCountry(counrtyName) :

    if counrtyName == other : 
        taxAmount = 0

    finalTotal = totalOrder + taxAmount
    print("Your total with tax is {0:.2f} " .format( finalTotal )) 

    return

def taxOnPerpose() :

    finalTotal = totalOrder + taxAmount


print("Your total with tax is {0:.2f} " .format( finalTotal )) 
