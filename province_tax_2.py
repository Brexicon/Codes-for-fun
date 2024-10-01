






counrtyName = input("Enter the country of oragine in : ")
    
    
amountOfSale = float((input("Enter the amount for the sale : ")))


def ifcounterycanada(counrtyName,amountOfSale):

    

    if counrtyName.lower() == "canada" :
    

        provinceName = input("Enter province name : ")


        if provinceName.lower() == "alberta" :
            taxAmount = 0.05 * amountOfSale
    
        elif provinceName.lower()  == "ontario" or \
             provinceName.lower() == "nova scotia" or\
             provinceName.lower() == "new brunswick" :
           taxAmount = 0.15 * amountOfSale
    
        elif provinceName.lower() == "quebec"  :
            taxAmount = 0.11 * amountOfSale

            taxAmount = amountOfSale * taxAmount

    else :
        taxAmount = amountOfSale

        
        
        print("The amount owed for tax is {0:.02f}" .format(taxAmount))

ifcounterycanada(counrtyName, amountOfSale)
            



print("Student name is Bradley R Horne")
print("Student number is W0410733")
        

