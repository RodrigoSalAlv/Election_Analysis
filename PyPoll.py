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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the reader row
    headers=next(file_reader)
    print(headers)

    # #Print each row in the CSV File
    # for row in file_reader:
    #     print(row)