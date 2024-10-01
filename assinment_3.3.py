



# this is my name: Brad Horne
# this is my Student Number: W0410733

#fist thing i do is look at what are my inputs (person sex, age of person, price of car)

#input

maleFemale = input("Are you male or female or other we do not judge : ")

ageOfOwner = float(input("How old are you : "))

carPrice = float(input("Enter the price of your car : "))


#next i look at how the math should (car price multiplied by percent that is divided one year or 12 months)
#then think of how to if statement everything. 
#proces

if ageOfOwner >= 40 and ageOfOwner < 70 :
    costForOwner = carPrice * (.1/12)


if maleFemale.lower() == "male" :

    if ageOfOwner >= 15 and ageOfOwner < 25 :
        costForOwner = carPrice * (.25/12)
    if ageOfOwner >= 25 and ageOfOwner < 40 :
        costForOwner = carPrice * (.17/12)
    

if maleFemale.lower() == "female" :

    if ageOfOwner >= 15 and ageOfOwner < 25 :
        costForOwner = carPrice * (.2/12)
    if ageOfOwner >=25 and ageOfOwner < 40 :
        costForOwner = carPrice * (.15/12)
    

elif maleFemale.lower() == "other" :
    
    if ageOfOwner >= 15 and ageOfOwner < 25 :
        costForOwner = carPrice * (.18/12)
    if ageOfOwner >=25 and ageOfOwner < 40 :
        costForOwner = carPrice * (.13/12)
    

#last is just making a print statement and how you want to format / word things out
#output

print("The cost for the owner every month is : ${0:.2f}"  .format(costForOwner))
