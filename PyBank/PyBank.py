import csv
import os

files_to_parse = ['budget_data_1.csv', 'budget_data_2.csv']
 
def process(reader):
    # frequency map (key = date, value = count)
    candidate_votes = {}
    for row in reader:
        # row[0] = voterid, row[1] = county, row[2] = candidate
        voterid = row[0]
        country = row[1]
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
    return candidate_votes


for file_name in files_to_parse:
    total_votes = {}
    file_path = os.path.join("Resources", file_name)

    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        candidate_votes = process(csvreader)
        for candidate, votes in candidate_votes.items():
            if candidate in total_votes:
                total_votes[candidate] += candidate_votes[candidate]
            else:
                total_votes[candidate] = candidate_votes[candidate]
        print(total_votes)
