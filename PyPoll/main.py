import os
import csv

csvpath = os.path.join("..", "Resources /", "election_data.csv")
outputfile = os.path.join("..", "Resources /", "Election——Results.txt")


with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    vote_count = 0
    candidates = []
    candidates_vote_count = {}
    winner = ""
    winner_votes = 0

    for row in csv_reader:
        vote_count += 1
        candidates_name = row[2]

        if row[2] not in candidates:
            candidates.append(row[2])
            candidates_vote_count[row[2]] = 0

        candidates_vote_count[row[2]] += 1


for elected_candidate in candidates_vote_count:

    votes = candidates_vote_count.get(elected_candidate)
    percentage = round(votes) / round(vote_count) * 100

    if (votes > winner_votes):
        winner_votes = votes
        winner = elected_candidate

    print(elected_candidate + ": " + str([percentage]) + '% (' + str(votes) + ')')


print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(vote_count))
print("-------------------------------------")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")


output_path = os.path.join("output", "PyPollAnsRedo.csv")

with open(output_path, 'w', newline='') as csvfile:

   csvwriter = csv.writer(csvfile, delimiter=',')

   csvwriter.writerow(['Election Results'])
   csvwriter.writerow(['----------------------------',])
   csvwriter.writerow(['Total Votes'])
   csvwriter.writerow(['----------------------------',])
   csvwriter.writerow(['Khan : '+str(percentage)+str(votes)])
   csvwriter.writerow(['Correy : '+str(percentage)+str(votes)])
   csvwriter.writerow(['Li : '+str(percentage)+str(votes)])
   csvwriter.writerow(['O Tooley : '+str(percentage)+str(votes)])
   csvwriter.writerow(['----------------------------',])
   csvwriter.writerow(['Winner : ' +'Khan'])
   csvwriter.writerow(['----------------------------',])