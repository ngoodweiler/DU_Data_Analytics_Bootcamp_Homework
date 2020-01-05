import os
import csv
budget_csv = os.path.join("Resources", "budget_data.csv")
month = []
profits = []
profit_change = []

#Read csv file
with open(budget_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#skip the header in calculations
    header = next(csvreader)
    #Check headers for remainder of code
    # print(f'headers {header}')

#Populate the month_count and total_profits lists
    for row in csvreader:
        month.append(str(row[0]))
        profits.append(int(row[1]))
    month_count = len(month)
    total_profits = sum(profits)

#For loop in the month_count list to get the profit % change and greatest increase/decrease values 
    for i in range(1,(month_count)):
        profit_change.append(int(profits[i] - profits[i-1]))

    greatest_increase = max(profit_change)
    greatest_decrease = min(profit_change)
    greatest_increase_month = ""
    greatest_decrease_month = ""
#Nested for loop to get the greatest increase/decrease months
    for j in range(len(profit_change)):
        if profit_change[j] == greatest_increase:
            greatest_increase_month = month[j+1]
        if profit_change[j] ==greatest_decrease:
            greatest_decrease_month = month[j+1]
#Final calculations to get the average profit change        
    sum_change = sum(profit_change)
    average_change = str(round(sum_change / (month_count-1),2))

#Print results to python
print('Financial Analysis')
print('------------------------------------------')
print(f"Total Months: {month_count}")
print(f"Total: ${total_profits}")
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
 
 #export text file
with open("Financial_Analysis.txt","w") as text_file:
    print('Financial Analysis',file=text_file)
    print('------------------------------------------',file=text_file)
    print(f"Total Months: {month_count}",file=text_file)
    print(f"Total: ${total_profits}",file=text_file)
    print(f'Average Change: ${average_change}',file=text_file)
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})',file=text_file)
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})',file=text_file)
text_file.close()