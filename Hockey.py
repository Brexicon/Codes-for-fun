


#input


teamName = input("Enter the Teams's Name : ")
teamWins = int(input("Enter the Team's Wins : "))
teamsLoses = int(input("Enter the Team's Loses : "))

#processing 


totalGames = teamWins + teamsLoses
numWins = teamWins / totalGames
numLoses = teamsLoses / totalGames

#output


print("The total games played was{0:.4f}". format(totalGames))
print("percent of WIns{0.4f}". format(numWins))
print("perecent of Loses{0.4f}". format(numLoses))