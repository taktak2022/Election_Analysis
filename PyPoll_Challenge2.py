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

# Create a list and dictionary of candidate options
candidate_options = []
candidate_votes = {}

# Create a list and dictionary for county votes.
county_options = []
county_votes = {}

# Track the winning candidate information.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the county voter and largest county turnout.
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes = total_votes + 1

        # Print the candidate name from each row.
        candidate_name = row [2]

        # Get the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # If the county does not match any existing county.
        if county_name not in county_options:

            # Add the county name to the county list.
            county_options.append(county_name)

            # Begin tracking the county's vote counts.
            county_votes[county_name] = 0

        # Add a vote to the county's total vote count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nELECTION RESULTS\n"
        f"-------------------------\n"
        f"TOTAL VOTES: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"RESULTS BY COUNTY:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # Determine the percentage and total votes for each county.  
    for county_name in county_votes:

        # Get the total county votes count.
        votes = county_votes[county_name]

        # Calculate percentage of votes per county.
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print county vote results.
        # print("\nCOUNTY RESULTS\n")
        county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results, end="")
        
        txt_file.write(county_results) #moved to here#

        if (votes > winning_county_count) and (vote_percentage > winning_county_percentage):
            winning_county_count = votes
            winning_county = county_name
            winning_county_percentage = vote_percentage

        # Print the winning county turnout information.
    largest_county_turnout = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n"
        f"\nSUMMARY OF CANDIDATE RESULTS:\n"
        )
    print(largest_county_turnout)

    #txt_file.write(winning_county)
    txt_file.write(largest_county_turnout) #added#
        
    # Determine the percentage of votes for each candidate.
    # 1 Iterate through the candidate list.
    print("\nCANDIDATE RESULTS\n")

    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes.get(candidate_name)
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # 4. Print the candidate name, vote count and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        txt_file.write(candidate_results) #added#
        
        # Determine winning vote count and candidate.
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage

            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    # Print out the winning candidate, vote count and vote percentage.
    winning_candidate_summary = (
        f"\n-------------------------\n"
        f"\nWINNING CANDIDATE SUMMARY:\n"
        f"WINNER: {winning_candidate}\n"
        f"WINNING VOTE COUNT: {winning_count:,}\n"
        f"WINNING PERCENTAGE: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
        )

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary) #added#

#with open(file_to_save, 'w') as txt_file:
    
#    txt_file.write(winning_candidate_summary)
#    txt_file.write(county_results)
#    txt_file.write(candidate_results) 

# Close the file.
election_data.close()
