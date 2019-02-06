import csv
import os

# Print title
print('Election Results')
print('------------------------------')

# direct path to budget data
electionPath = os.path.join('election_data.csv')

# open budgetPath as read file
with open(electionPath, newline='') as electionFile:
    # specify delimiter
    electionReader = csv.reader(electionFile, delimiter=',')

    # set counter to 0
    totalVotes = 0
    countyTotal = 0
    khan = 0
    correy = 0
    li = 0
    otooley = 0

    # set lists for columns
    county = []
    candidate = []

    # skip header line when calculating profit/loss total
    header = next(electionReader)

    # loop through rows to calculate total # of votes
    for row in electionReader:
        totalVotes += len(row[1])
        
        # Khan totals
        if row[1] == "Kahn":
            khan+=1

        # Correy totals
        if totalVotes == "Correy":
            correy+=1

        # Li Totals
        if totalVotes == "Li":
            li+=1
        
        # O'Tooley Totals
        if totalVotes == "O'Tooley":
            otooley+=1
        

        khan_percent = (khan / totalVotes) * 100
        correy_percent =(correy / totalVotes) * 100
        li_percent = (li / totalVotes) * 100
        otooley_percent = (otooley / totalVotes) * 100

    print('Total Votes: ' , totalVotes)
    print('-------------------------------')
    print('Khan : ' , khan_percent,'%')
    print('Correy : ' , correy_percent,'%')
    print('Li : ' , li_percent,'%')
    print('OTooley : ' , otooley_percent,'%')
    file = open("py_poll.txt" , 'w')
    file.write('file')