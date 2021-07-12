# NU Data Science Boot Camp, Summer 2021 Session, Week 3 Homework: Python Challenge
# Written by Seong-Min Kim, Date: July 15, 2021

# Imports modules
import os
import csv

# Creates path to the data file
csvpath = os.path.join("budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Read the header row first
    csv_header = next(csvreader)
    # Then count the entire rows after the header. This calculates the total months
    total = 0

    for row in csvreader:
        print(row)
        total_months = len(list(csvreader))
        total = total + int(row[1])
        

