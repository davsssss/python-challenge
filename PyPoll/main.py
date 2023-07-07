import os
import csv

#set local path
dataset = os.path.join(r'..\election_data.csv')
output_file = r"C:..\pollanalysis.txt"
#dictionary for candidate votes
candidatevotes = {}
#opens and reads csv file 
with open(dataset, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header
    csv_header = next(csvreader)
    #iterates through csv
    for row in csvreader:
        #locates candidate column
        candidate = row[2]
        #tracks candidate along with their votes
        if candidate not in candidatevotes:
            candidatevotes[candidate] = 1
        else:
            candidatevotes[candidate] += 1

#tally final votes
values = candidatevotes.values()
final_vote = sum(values)

#print results
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {final_vote}")
print(f"-------------------------")
for name, value in candidatevotes.items():
    print(f"{name}: {value / final_vote:.3%} ({value})")
print(f"-------------------------")
print(f"Winner: {max(candidatevotes, key=candidatevotes.get)}")
print(f"-------------------------")

# write to text file
with open(output_file, "w") as text:
    text.write(f"Election Results\n")
    text.write(f"-------------------------\n")
    text.write(f"Total Votes: {final_vote}\n")
    text.write("-------------------------\n")
    for name, value in candidatevotes.items():
        text.write(f"{name}: {value / final_vote:.3%}  ({value})\n")
    text.write(f"-------------------------\n")
    text.write(f"Winner: {max(candidatevotes, key=candidatevotes.get)}\n")
    text.write(f"-------------------------\n")

