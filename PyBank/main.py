#import dependencies
import csv
import os

#load files to read and output
budget_data = os.path.join("Resources", "budget_data.csv")
analysis_conclusion = os.path.join("analysis", "analysis.txt")

#create parameters
month_total = 0
net_total = 0
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
month_of_change = []

#read csv file
with open(budget_data) as csvfile:
    reader = csv.reader(csvfile)

    header = next(reader)
    
    first_row = next(reader)
    month_total += 1
    net_total += int(first_row[1])
    prev_net = int(first_row[1])
    
    #loop through csvfile
    for row in reader:

        #track total
        month_total += 1
        net_total += int(row[1])

        #track net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        #get greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        #get greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

#average net change
net_monthly_average = sum(net_change_list) / len(net_change_list)

#generate output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {month_total}\n"
    f"Total: ${net_total}\n"
    f"Average  Change: ${net_monthly_average:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

#print to terminal
print(output)

#export to txt file
with open(analysis_conclusion, "w") as txt_file:
    txt_file.write(output)


