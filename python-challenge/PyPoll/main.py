import os
import csv
budget_csv = os.path.join("Resources", "election_data.csv")
voter_id = []
candidate_raw = []

#Read csv file
with open(budget_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Skip the header in calculations
    header = next(csvreader)

#Populate total_votes and candidates list
#Used the set() function to get the candidates from the data as a check on list from the instructions
    for row in csvreader:
        voter_id.append(str(row[0]))
        candidate_raw.append(str(row[2]))
    total_votes = len(voter_id)
    candidate_set = set(candidate_raw)
    candidates = list(candidate_set)
#print(candidates)
#based on the candidates found from above print (now just noted), candidates are O'Tooley, Correy, Li, Khan
#Create and populate the lists for each candidate's vote count
    OTooley_votes = []
    Correy_votes = []
    Li_votes = []
    Khan_votes = []
    for i in range(total_votes):
        if candidate_raw[i] == "O'Tooley":
            OTooley_votes.append(candidate_raw[i])
        elif candidate_raw[i] =='Correy':
            Correy_votes.append(candidate_raw[i])
        elif candidate_raw[i] == 'Li':
            Li_votes.append(candidate_raw[i])
        else:
            Khan_votes.append(candidate_raw[i])
#Total vote counts and percent based on the lists above
OTooley_vote_count = len(OTooley_votes)
Correy_vote_count = len(Correy_votes)
Li_vote_count = len(Li_votes)
Khan_vote_count = len(Khan_votes)
OTooley_percent = float(round(len(OTooley_votes) / total_votes * 100,3))
Correy_percent = float(round(len(Correy_votes) / total_votes * 100,3))
Li_percent = float(round(len(Li_votes) / total_votes * 100,3))
Khan_percent = float(round(len(Khan_votes) / total_votes * 100,3))

#If/Else to determine the winner without looking at the data myself
if OTooley_percent > (Correy_percent and Li_percent and Khan_percent):
    winner = "O'Tooley"
elif Correy_percent > (OTooley_percent and Li_percent and Khan_percent):
    winner = 'Correy'
elif Li_percent > (OTooley_percent and Correy_percent and Khan_percent):
    winner = 'Li'
else:
    winner = 'Khan'

#Print results to python
print('------------------------------')
print('Election Results')
print('------------------------------')
print(f'Total Votes: {total_votes}')
print('------------------------------')
print(f'Khan: {Khan_percent}% ({Khan_vote_count})')
print(f'Correy: {Correy_percent}% ({Correy_vote_count})')
print(f'Li: {Li_percent}% ({Li_vote_count})')
print(f"O'Tooley: {OTooley_percent}% ({OTooley_vote_count})")
print('------------------------------')
print(f'Winner: {winner}')
print('------------------------------')
#export text file
with open("Election_results.txt","w") as text_file:
    print('------------------------------',file=text_file)
    print('Election Results',file=text_file)
    print('------------------------------',file=text_file)
    print(f'Total Votes: {total_votes}',file=text_file)
    print('------------------------------',file=text_file)
    print(f'Khan: {Khan_percent}% ({Khan_vote_count})',file=text_file)
    print(f'Correy: {Correy_percent}% ({Correy_vote_count})',file=text_file)
    print(f'Li: {Li_percent}% ({Li_vote_count})',file=text_file)
    print(f"O'Tooley: {OTooley_percent}% ({OTooley_vote_count})",file=text_file)
    print('------------------------------',file=text_file)
    print(f'Winner: {winner}',file=text_file)
    print('------------------------------',file=text_file)
text_file.close()