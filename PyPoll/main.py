#import dependencies
import os
import csv

#load file and output path
election_data = os.path.join("Resources", "election_data.csv")
election_analysis = os.path.join("analysis", "analysis.txt")

#count total votes
total_votes = 0

#candidate options and vote counters
candidates = []
canditate_votes = {}

#winning candidate and winning count tracker
winner = ""
winning_count = 0

#read csv and convert to list of dictionaries
with open(election_data) as csvfile:
    reader = csv.reader(csvfile)

    #read header
    header = next(reader)

    #loop through rows
    for row in reader:
        total_votes = total_votes + 1

        #extract candidate name from each row
        candidate_name = row[2]

        #if candidate does not match any existing candidate
        if candidate_name not in candidates:
            
            #add candidate name to list
            candidates.append(candidate_name)

            #begin tracking said candidates voter count
            canditate_votes[candidate_name] = 0

        #add vote to candidates count
        canditate_votes[candidate_name] = canditate_votes[candidate_name] + 1

#print results and export to text file
with open(election_analysis, "w") as txt_file:

    #print final vote count
    election_results = (
        f"\n\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"---------------------------\n"
    )
    print(election_results)

    txt_file.write(election_results)

    #loop through counts to determine the winner
    for candidate in canditate_votes:
        votes = canditate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        #get winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)

        txt_file.write(voter_output)

    #print winner
    winning_candidate_summary = (
        f"----------------------------\n"
        f"WINNER: {winning_candidate}\n"
        f"----------------------------\n"
    )
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)