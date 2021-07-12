# NU Data Science Boot Camp, Summer 2021 Session, Week 3 Homework: Python Challenge/PyPoll
# Written by Seong-Min Kim, Date: July 15, 2021

# Imports modules
import os
import csv

# Creates path to the data file
csvpath = os.path.join("test.csv")

total_votes = []
candidate_list = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

     # Read and store the header row first
    csv_header = next(csvreader)
    
    # Start the interation
    for row in csvreader:
       # Store the number of entries the csv resource file into a list 
        total_votes.append(row[0])
        candidate_list.append(row[2])
        def unique(candidate_list):
           unique_candidates = []
           for x in candidate_list:
               if x not in unique_candidates:
                   unique_candidates.append(x)
        print(unique_candidates)


print(len(total_votes))
print(unique(candidate_list))
