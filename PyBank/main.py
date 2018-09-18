import os
import csv 

csvpath = os.path.join("..", "Resources /", "budget_data.csv")
outputfile = os.path.join("..", "Resources /", "Financial Analysis.txt")

with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    month_count = 0
    total_profit = 0
    profit_inc = ["", 0]
    loss_dec = ["", 8897553]
    change_m = []

    row = next(csv_reader)
    previous_value = int(row[1])
    total_profit = total_profit + int(row[1])

    for row in csv_reader:
        month_count += 1
        total_profit += int(row[1])
        change_value = total_profit - previous_value
        previous_value = int(row[1])
        change_m = change_m + [row[0]]

        if change_value >= profit_inc[1]:
            profit_inc[0] = row[0]
            profit_inc[1] = change_value

        elif change_value <= loss_dec[1]:
            loss_dec[0] = row[0]
            loss_dec[1] = change_value

avg = str(round(change_value / (month_count-1),2))

print("Financial Analysis")
print("---------------------")
print("Total Months: " + str(month_count))
print("Total Revenue: $" + str(total_profit))
print("Average Change: $" + str(avg))
print("Greatest Increase in Profits: " + profit_inc[0] + " ($" + str(profit_inc[1]) + ")")
print("Greatest Decrease in Profits: " + loss_dec[0] + " ($" + str(loss_dec[1]) + ")")

output_path = os.path.join("output", "PyBankAns.csv")

with open(output_path, 'w', newline='') as csvfile:

   csvwriter = csv.writer(csvfile, delimiter=',')

   csvwriter.writerow(['Financial Analysis-----------------',])
   csvwriter.writerow(['Total Months : '+str(month_count)])
   csvwriter.writerow(['Total : ' +str(total_profit)])
   csvwriter.writerow(['Average Change : '+str(avg)])
   csvwriter.writerow(['Greatest Increase in Profits : ' +str(profit_inc)])
   csvwriter.writerow(['Greatest Decrease in Profits : ' +str(loss_dec)])