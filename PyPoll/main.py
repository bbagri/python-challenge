import os
import csv

csvpath = os.path.join("..", "Resources /", "election_data.csv")
outputfile = os.path.join("..", "Resources /", "Election——Results.txt")

total_votes = 0

candidates = []
candidates_votecount = {}

winner = ""
winner_votecount = 0

with open(csvpath) as rawdata:
    reader = csv.reader(rawdata)
    header = next(reader)

    for row in reader:

        total_votes += 1
        
        candidates_name = row[2]

        if candidates_name not in candidates:

            candidates.append(candidates_name)
            candidates_votecount[candidates_name] = 0

        candidates_votecount[candidates_name] += 1

with open(outputfile, "w") as txt_file:

    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

    for x in candidates_votecount:

        votes = candidates_votecount.get(x)
        percenatge_count = float(votes) / float(total_votes) * 100

        if (votes > winner_votecount):
            winner_votecount = votes
            winner = x

        listofresults = f"{x}: {percenatge_count:.3f}% ({votes})\n"
        print(listofresults, end="")

        txt_file.write(listofresults)

    election_results_part2 = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")
    print(election_results_part2)

    txt_file.write(election_results_part2)



    # Specify the file to write to
output_path = os.path.join("output", "PyPollAns.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

   # Initialize csv.writer
   csvwriter = csv.writer(csvfile, delimiter=',')

   # Write the first row (column headers)
   csvwriter.writerow(['Election Results'])
   # Write the second row
   csvwriter.writerow(['----------------------------',])
   csvwriter.writerow(['Total Votes'])
   csvwriter.writerow(['----------------------------',])

   csvwriter.writerow(['Khan : '+str(percenatge_count)+str(votes)])
   csvwriter.writerow(['Correy : '+str(percenatge_count)+str(votes)])
   csvwriter.writerow(['Li : '+str(percenatge_count)+str(votes)])
   csvwriter.writerow(['O Tooley : '+str(percenatge_count)+str(votes)])
   csvwriter.writerow(['----------------------------',])
   csvwriter.writerow(['Winner : ' +'Khan'])
   csvwriter.writerow(['----------------------------',])