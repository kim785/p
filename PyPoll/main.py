# NU Data Science Boot Camp, Summer 2021 Session, Week 3 Homework: Python Challenge/PyPoll
# Written by Seong-Min Kim, Date: July 15, 2021

# Imports modules
import os
import csv

# Creates path to the data file
csvpath = os.path.join("Resources/election_data.csv")

total_votes = []
candidate_list = []
unique_candidates = []
vote_count = [0,0,0,0]
vote = 0
i = 0
vote_percentage = [0,0,0,0]
j = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

     # Read and store the header row first
    csv_header = next(csvreader)
    
     # Start the iteration
    for row in csvreader:

         # Store the number of entries the csv resource file into a list 
        total_votes.append(row[0])
        candidate_list.append(row[2])
        
    # Make a function that will identify unique values of candidate_list
    for x in candidate_list:
        if x not in unique_candidates:
            unique_candidates.append(x) # print(unique_candidates) will output ['Khan', 'Correy', 'Li', "O'Tooley"]
    
    # Another loop that will count votes and percentage of each candidate
    while i < len(unique_candidates):
        for x in candidate_list:
            if x == unique_candidates[i]:
                vote = vote + 1
        vote_count[i] = vote # print(vote_count) will output [2218231, 704200, 492940, 105630]
        vote_percentage[i] = format(100 * vote/len(total_votes), ".3f") # print(vote_percentage) will output ['63.000', '20.000', '14.000', '3.000']
        i = i + 1 # compute for next i
        vote = 0  # resets vote count for the next candidate
    
    max_vote = max(vote_count) # find the greatest number of votes
    max_index = int(vote_count.index(max_vote))  # find the index of max_vote
    Winner = unique_candidates[max_index]    # now find the candidate name who corresponds to max_index

    # Print the output
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {len(total_votes)}")
    print("-------------------------")
    while j < 4: # Instead of 4, we could also do len(unique_candidates)
        print(f"{unique_candidates[j]}: {vote_percentage[j]}% ({vote_count[j]})") 
        j = j + 1   
    print("-------------------------")
    print(f"Winner: {Winner}")

# Now export the result:
output_path = os.path.join("analysis/Results.txt")

with open(output_path, "w", newline="") as textfile:
    
    print("Election Results", file = textfile)
    print("-------------------------", file = textfile)
    print(f"Total Votes: {len(total_votes)}", file = textfile)
    print("-------------------------", file = textfile)
    print(f"{unique_candidates[0]}: {vote_percentage[0]}% ({vote_count[0]})", file = textfile)
    print(f"{unique_candidates[1]}: {vote_percentage[1]}% ({vote_count[1]})", file = textfile)
    print(f"{unique_candidates[2]}: {vote_percentage[2]}% ({vote_count[2]})", file = textfile)
    print(f"{unique_candidates[3]}: {vote_percentage[3]}% ({vote_count[3]})", file = textfile) 
    print("-------------------------", file = textfile)
    print(f"Winner: {Winner}", file = textfile)
