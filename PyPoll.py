# The date we need to retrieve.
# 1. The Total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Create a list of candidate options
candidate_options = []

# Create a dictionary for candidate votes.
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open('c:/users/Takemi Scott Oshiro/Election_Analysis/Resources/election_results.csv') as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes = total_votes + 1

        # Print the candidate name from each row.
        candidate_name = row [2]

        # If the candidate does not match any existing candidate.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
with open('c:/users/Takemi Scott Oshiro/Election_Analysis/analysis/election_analysis.txt', 'w') as txt_file:


# Determine the percentage of votes for each candidate.
# 1 Iterate through the candidate list.
    for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
        votes = candidate_votes.get(candidate_name)
    # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

# 4. Print the candidate name, vote count and percentage of votes.
        candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

# Save and print the results to our text file.
        txt_file.write(candidate_results)

    # Determine winning vote count and candidate.
    # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

# Save the results to our text file.
#with open('c:/users/Takemi Scott Oshiro/Election_Analysis/analysis/election_analysis.txt', 'w') as txt_file:

# Print out the winning candidate, vote count and vote percentage.
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")

# Print the Winning Candidate Summary.
print(winning_candidate_summary)

# 3. Print the total votes.
print("The total number of votes is ", total_votes)

# Save the candidate results to our text file.
with open('c:/users/Takemi Scott Oshiro/Election_Analysis/analysis/election_analysis.txt', 'w') as txt_file:

    txt_file.write(winning_candidate_summary)        

# Close the file.
    election_data.close()
