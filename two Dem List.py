




# peopleInfo = [["Yousef", 1500, "hali", 2],
#                 ["brad", 2500, "dart", 0],
#                 ["will", 12, "timber", 15],
#                 ["JACK", 10000, "hali", 25]]

empInfo = [] #this is an empty 2 dim list
#the one dim list 
# it will contain one employee's information 


numOfEmp = int(input("What is the number of employee's : "))

for i in range (numOfEmp):
    tempInfo = [] # empty one dim list 
    empName = input("Enter the empName \t:")
    empAdd = input("Enter the emp. Salary :")
    empSal = input("Enter the emp. Address :")
    empKids = input("Enter the emp. Number of kids :")

    tempInfo.append(empName)
    tempInfo.append(empAdd)
    tempInfo.append(empSal)
    tempInfo.append(empKids)
    

