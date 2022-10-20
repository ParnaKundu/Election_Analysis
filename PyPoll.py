# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The total number of votes each candidate won
# 4. The percentage of votes each candidate won
# 5. The winner of the election based on the popular vote.

# Add our dependencies

import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Process each row in the csv file
    for row in file_reader:

        # Add to the total vote count
        total_votes += 1

        # Get candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate, add it to the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Begin tracking each candidates vote
            candidate_votes[candidate_name] = 0
        
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the total vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    #Save the final count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}: {vote_percentage : .1f}% ({votes : ,})\n" )
        # Print each candidate, their voter count and percentage to the terminal
        print(candidate_results)

        # Save the candidate results to the text file
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Print the winning candidate's result to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count: ,}\n"
        f"Winning Percentage: {winning_percentage: .1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)