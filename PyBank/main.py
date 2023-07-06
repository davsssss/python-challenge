import os
import csv

#set local path
dataset = os.path.join(r'C:\Users\bando\python-challenge\PyBank\Resources\budget_data.csv')
output_file = r"C:\Users\bando\python-challenge\PyBank\Analysis\bankanalysis.txt"

num_months = []
currency = []
change_profit = []

#open and read csv
with open(dataset,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #skip header
    header = next(csvreader)
    
                      
    #iterate through the rows to find the change in profit and add to change_profit[] 
    for row in csvreader:
        num_months.append(row[0])
        currency.append(int(row[1]))
    for i in range(len(currency)-1):
        change_profit.append(currency[i+1]-currency[i])
                      
#find min and max from change_profit
increase = max(change_profit)
decrease = min(change_profit)

#fix list index values
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1


#print results
print(f"Financial Analysis\n")
print(f"-------------------------\n")
print(f"Total Months: {len(num_months)}")
print(f"Total: ${sum(currency)}")
print(f"Average Change: ${round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {num_months[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {num_months[month_decrease]} (${(str(decrease))})")   


# write to text file
with open(output_file, "w") as text:
    text.write(f"Financial Analysis\n")
    text.write(f"----------------------------\n")
    text.write(f"Total Months: {len(num_months)}\n")
    text.write(f"Total: ${sum(currency)}\n")
    text.write(f"Average Change: ${round(sum(change_profit)/len(change_profit),2)}\n")
    text.write(f"Greatest Increase in Profits: {num_months[month_increase]} (${(str(increase))})\n")
    text.write(f"Greatest Decrease in Profits: {num_months[month_decrease]} (${(str(decrease))})")