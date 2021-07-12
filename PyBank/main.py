# NU Data Science Boot Camp, Summer 2021 Session, Week 3 Homework: Python Challenge/PyBank
# Written by Seong-Min Kim, Date: July 15, 2021

# Imports modules
import os
import csv

# Creates path to the data file
csvpath = os.path.join("Resources/budget_data.csv")

# Empty lists and the initial values for each variable
total_months = []
total = 0
value = 867884
total_list = []
change_list = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Read and store the header row first
    csv_header = next(csvreader)
    
    # Start the interation
    for row in csvreader:

        # Store the "Date" column of the csv resource file into a list 
        total_months.append(row[0])

        # Add up the profit/losses
        total = total + int(row[1])

        # Stores the "Profit/Losses" column of the csv resource file into a list in the form of integer, not string
        total_list.append(int(row[1]))
    
    # While loop that calculates the difference of two rows. "Change" is stored in a list called "change_list"
    i = 1
    while i < len(total_list):
        change = total_list[i] - value
        change_list.append(change)
        value = total_list[i]
        i += 1
    
    # Then, find the average. Sum of the "change_list" divided by the number of entries.
    average_change = sum(change_list)/len(change_list)
    
    # Finds the greatest increase in profit 
    max_change = max(change_list)

    # Finds the index of the greatest increase in profit
    max_index = 1 + int(change_list.index(max_change))

    # Finds the greatest decrease in profit
    min_change = min(change_list)

    # Finds the index of the greatest decrease in profit
    min_index = 1 + int(change_list.index(min_change))

    # Now, print the result:
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(total_months)}")
    print(f"Total: ${total}")
    print(f"Average Change: ${round(average_change, 2)}")
    print(f"Greatest Increase in Profits: {total_months[max_index]} (${max_change})")
    print(f"Greatest Decrease in Profits: {total_months[min_index]} (${min_change})")

# Now export the result:
output_path = os.path.join("analysis/Results.txt")

with open(output_path, "w", newline="") as textfile:

    print("Financial Analysis", file = textfile)
    print("----------------------------", file = textfile)
    print(f"Total Months: {len(total_months)}", file = textfile)
    print(f"Total: ${total}", file = textfile)
    print(f"Average Change: ${round(average_change, 2)}", file = textfile)
    print(f"Greatest Increase in Profits: {total_months[max_index]} (${max_change})", file = textfile)
    print(f"Greatest Decrease in Profits: {total_months[min_index]} (${min_change})", file = textfile)
