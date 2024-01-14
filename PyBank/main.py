# import libraries
import os
import csv

# Read csv file
csv_file = os.path.join('Resources','budget_data.csv')

# Create empty list for month & profit/loss data
month = []
profit_loss_mth = []

# Read in the CSV file
with open(csv_file, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Get header row
    header = next(csvreader)

    # Create list of each column
    for row in csvreader:
        month.append(row[0])
        profit_loss_mth.append(int(row[1]))  
    
    # Get total profit loss
    profit_loss_total = sum(profit_loss_mth)

    # Get difference in profit loss from month to month
    # 1. https://www.geeksforgeeks.org/python-generate-successive-element-difference-list/
    profit_loss_diff = [profit_loss_mth[i + 1] - profit_loss_mth[i] for i in range(len(profit_loss_mth)-1)]

    # Get average profit/loss change from month to month   
    avg_profit_loss_diff = sum(profit_loss_diff) / len(profit_loss_diff)
    
    # Get greatest increase in profits (date and amount) over the entire period
    greatest_profit_loss = max(profit_loss_diff)
    index_max_profit_loss = profit_loss_diff.index(greatest_profit_loss)
    month_max_profit_loss = month[index_max_profit_loss+1]

    
    # Get greatest decrease in profits (date and amount) over the entire period
    lowest_profit_loss = min(profit_loss_diff)
    index_min_profit_loss = profit_loss_diff.index(lowest_profit_loss)
    month_min_profit_loss = month[index_min_profit_loss+1]

# Get total number of months in file
with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    # Get number of months/rows in csv file
    list_csv = list(csvreader)
    number_months = len(list_csv)

    
# Print results of financial analysis
print('Financial Analysis')
print(' ')
print('-----------------------------------------------')
print(' ')
print("Total Months: " + str(number_months)) 
print("Total: $" + str(profit_loss_total))
print("Average Change: $" + "{:.2f}".format( avg_profit_loss_diff )) # 2. https://www.askpython.com/python/built-in-methods/format-2-decimal-places
print(f'Greatest Increase in Profits: {month_max_profit_loss} (${str(greatest_profit_loss)})')
print(f'Greatest Decrease in Profits: {month_min_profit_loss} (${str(lowest_profit_loss)})')


# Export text file with results
f = open('analysis/Financial_Analysis.txt', 'w')
f.write('Financial Analysis')
f.write('\n') # 3. https://www.pythontutorial.net/python-basics/python-write-text-file/
f.write('\n')
f.write('-----------------------------------------------')
f.write('\n')
f.write('\n')
print("Total Months: " + str(number_months), file=f) # 4. https://blog.enterprisedna.co/python-write-to-file/
f.write('\n')
print("Total: $" + str(profit_loss_total), file=f)
f.write('\n')
print("Average Change: $" + "{:.2f}".format( avg_profit_loss_diff ), file=f)
f.write('\n')
print(f'Greatest Increase in Profits: {month_max_profit_loss} (${str(greatest_profit_loss)})', file=f)
f.write('\n')
print(f'Greatest Decrease in Profits: {month_min_profit_loss} (${str(lowest_profit_loss)})', file=f)
f.close()