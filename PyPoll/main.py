# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyPoll", "Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("PyPoll", "analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
winner = " "
max_votes = 0
# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}

# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets) - commented out b/c does not match with challange example output.
        #print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        
        candidate_votes[candidate] += 1

# Open a text file to save the output


    # Print the total vote count (to terminal)
    print("\nElection Results")
    print("--------------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------------")

    for candidate, votes in candidate_votes.items():
        percentage = (votes/total_votes)*100
        print(f"{candidate}: {percentage:.3f}% ({votes})")

        #Count winning votes
        if votes > max_votes:
            max_votes = votes
            winner = candidate

    print("--------------------------------")
    print(f"Winner: {winner}")
    print("--------------------------------")

#with open(file_to_output, "w") as txt_file:
    # Write the total vote count to the text file
    #txt_file.write("Election Results")
    #txt_file.write("--------------------------------")
    #txt_file.write(f"Total Votes: {total_votes}")
    #txt_file.write("--------------------------------")


    # Loop through the candidates to determine vote percentages and identify the winner


        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage


    # Generate and print the winning candidate summary


    # Save the winning candidate summary to the text file hello
