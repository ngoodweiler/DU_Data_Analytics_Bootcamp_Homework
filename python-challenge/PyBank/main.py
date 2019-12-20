import os
import csv
budget_csv = os.path.join("Resources", "budget_data.csv")

month_counter = 0
total_profit = 0
month = []
profits = []

with open(budget_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    #setting month and profits as lists
    for row in csvreader:
        month.append(str(row[0]))
        profits.append(float(row[1]))

    for row1 in csvreader:
        if row1[0] > str(0):
            month_counter = month_counter + 1
            total_profit = total_profit + int(row1[1])

    current_profit = float()
    previous_profit = float()
    profit_change = current_profit - previous_profit
    for profit in csvreader:
        current_profit = float(profit[1])
        if profit_change[1] > profit_change[-1]:
            profit_change = profit_change[1]
        else:
            profit_change = profit_change[-1]
        previous_profit = current_profit



print(f'{month}')
print(f'{profits}')
print(f'{profit_change}')
print(f"Total Months: {month_counter}")
print(f"Total: ${total_profit}")

        