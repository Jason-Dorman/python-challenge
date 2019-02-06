import os
import csv

# Print title
print('Financial Analysis')
print('------------------------------')

# direct path to budget data
bugdetPath = os.path.join('budget_data.csv')

# open budgetPath as read file
with open(bugdetPath, newline='') as budgetFile:
    # specify delimiter
    budgetReader = csv.reader(budgetFile, delimiter=',')

    # set counter to 0
    revenue = 0
    totalMonths = 0
    monthlyChange = 0
    previousrow = 0
    counter = 0
    max_increase = 0
    ##max_increase_date = None
    min_decrease = 0
    #min_decrease_date = None

    # skip header line when calculating profit/loss total
    header = next(budgetReader)

    # loop through rows to calculate profit/loss & month total
    for row in budgetReader:
        revenue += int(row[1])

    # calculate total number of months
        totalMonths += 1

        if counter == 0:
           lastrow = int(row[1])
           counter +=1
        else:
            change = int(row[1])-lastrow
            monthlyChange +=change
            lastrow = int(row[1])

            if max_increase ==0 or change < max_increase:
                max_increase = change
                #max_increase_date = date
            if min_decrease ==0 or change < min_decrease:
                min_decrease = change
                #min_decrease_date = date
    
    # print
    print('Total Months: ' , totalMonths)
    print('Total: ' , '$' , revenue)
    print('Average Change: ' , '$',round((monthlyChange / (totalMonths-1)),2))
    print('Greatest Increase in Profits' , '$' , max_increase)
    print('Greatest Decrease in Profits' , '$' , min_decrease)
    file = open("py_bank.txt" , 'w')
    file.write('file')