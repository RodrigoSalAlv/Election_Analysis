#The data need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

#     # Print the file object.
#      print(election_data)




# # # Using the open() function with the "w" mode we will write data to the file.
# # open(file_to_save, "w")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
    # txt_file.write("Hello World, ")
    # txt_file.write("Araphoe")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson, ")
    #To add new lines we write \n after each word we want in a new line
    # txt_file.write("Counties in the election\n-----------------\nAraphoe\nDenver\nJefferson")

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load="Module 3 Python/Election_Analysis/Resources/election_results.csv"
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Module 3 Python","Election_Analysis","analysis", "election_analysis.txt")

total_votes=0
candidate_options=[]
candidate_votes={}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the reader row
    headers=next(file_reader)

    #Print each row in the CSV File
    for row in file_reader:
        #get the total of votes (The standard Python format to increment a variable is number = number + 1, which can be augmented to number += 1.)
        total_votes += 1
        #get the name of the candidate in each row
        candidate_name = row[2]
       
        if candidate_name not in candidate_options:
            #add the names of each candidate to the candidate_options list if the candidate is not in already
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name]=0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1


#Print Total_Votes
# print(total_votes)
# print(candidate_options)
# print(candidate_votes)

for candidate_name in candidate_votes:
    #Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    #Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    #Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.2f}% ({votes:,} votes)\n")

    if (votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count=votes
        winning_percentage=vote_percentage
        winning_candidate=candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")    

print(winning_candidate_summary)
