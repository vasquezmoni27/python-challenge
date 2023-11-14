import csv

#Declare variables
Months = 0
Winner = ""
Candidate1 = "Charles Casper Stockham"
Candidate2 = "Diana DeGette"
Candidate3 = "Raymon Anthony Doane"
Vote1 = 0
Vote2 = 0
Vote3 = 0


#import and open csv
with open('election_data.csv', 'r') as csvfile:
    file = csv.reader(csvfile)

    
# Skip the header row
    next(file, None)

#Process CSV data
    for row in file:
        Total += 1

        if row[2] == Candidate1:
            Vote1 += 1
        elif row[2] == Candidate2:
            Vote2 += 1
        elif row[2] == Candidate3:
            Vote3 += 1

# Determine winner
    if Vote1 > Vote2 and Vote1 > Vote3:
        Winner = Candidate1
    elif Vote2 > Vote1 and Vote2 > Vote3:
        Winner = Candidate2
    elif Vote3 > Vote1 and Vote3 > Vote2:
        Winner = Candidate3

print ("Election Results")
print ("----------------------------")
print ("Total Votes", Total)
print ("Charles Casper Stockham:", Candidate1)
print ("Diana DeGette:", Candidate2)
print ("Raymon Anthony Doane:", Candidate3)
print ("Winner:", Winner)  