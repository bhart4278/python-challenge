# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyBank", "Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("PyBank", "analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
net_change_list = []
previous_profit = None
greatest_increase = ("", 0)
greatest_decrease = ("", 0)

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    

    # Track the total and net (profit) change

    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1

        # Track the net change - calling value of the row in column 1
        current_profit = int(row[1])
        total_net += current_profit

        if previous_profit is not None:
            change = current_profit - previous_profit
            net_change_list.append(change)

        # Calculate the greatest increase in profits (month and amount)
            if change > greatest_increase[1]:
                greatest_increase = (row[0], change)

        # Calculate the greatest decrease in losses (month and amount)
            if change < greatest_decrease[1]:
                greatest_decrease = (row[0], change)

        #updates previous profit
        previous_profit = current_profit


# Calculate the average net change across the months
average_net_change = sum(net_change_list)/len(net_change_list) if net_change_list else 0

# Generate the output summary


# Print the output to terminal
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${average_net_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Write the results to a text file budget_analysis.txt
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("-----------------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average Change: ${average_net_change}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
