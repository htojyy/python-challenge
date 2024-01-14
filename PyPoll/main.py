# import libraries
import os
import csv

# Read csv file
csv_file = os.path.join('Resources','election_data.csv')

# Create empty list for ballot ID, county and candidate data
ballot_id = []
county = []
candidate = []

# Read in the CSV file
with open(csv_file, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Get header row
    header = next(csvreader)
    
    # Create list of each column
    for row in csvreader:
        ballot_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    
    # Get unique list of candidates
    uniq_candidates = set(candidate)
    uniq_candidates_list = list(uniq_candidates)
    number_candidates = len(uniq_candidates_list)
    
# Get total votes overall
with open(csv_file, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    # Get number of rows/votes in csv file
    list_csv = list(csvreader)
    number_votes = len(list_csv)
    
# Dynamically get count of votes for each candidate
# 5. https://python.plainenglish.io/how-to-dynamically-declare-variables-inside-a-loop-in-python-21e6880aaf8a
dict_count = {}
for i in range(number_candidates):
    key = uniq_candidates_list[i]
    # Variables to keep track of each count
    dict_count[key] = 0
    # Get total votes per candidate
    # 6. https://discuss.codecademy.com/t/is-it-possible-to-count-the-occurrences-of-multiple-items-in-a-list-using-a-single-loop/377325 
    for element in candidate:
        if element == uniq_candidates_list[i]:
             dict_count[key] += 1

 # Dynamically get pct of votes for each candidate, formatted to 3 decimal places 
dict_pct = {}
for i in range(number_candidates):
    key = uniq_candidates_list[i]
    dict_pct[key] = 0
    dict_pct[key] = "%.3f" % float(dict_count[uniq_candidates_list[i]] / number_votes * 100) #2. https://www.askpython.com/python/built-in-methods/format-2-decimal-places

# Get winner's name
# 7. https://note.nkmk.me/en/python-dict-value-max-min/
winner_name = max(dict_count, key=dict_count.get)



# Print results of election results
print('Election Results')
print(' ')
print('-----------------------------------------------')
print(' ')
print("Total Votes: " + str(number_votes)) 
print(' ')
print('-----------------------------------------------')
print(' ')

# Dynamically print candidate name, % of votes and # votes
# 8. https://stackoverflow.com/questions/15114843/accessing-dictionary-value-by-index-in-python
for i in range(number_candidates):
    print(f'{uniq_candidates_list[i]}: {list(dict_pct.values())[i]}% ({list(dict_count.values())[i]})')

print(' ')
print('-----------------------------------------------')
print(' ')
print(f'Winner: {winner_name}')
print(' ')
print('-----------------------------------------------')


# Export text file with results
f = open('analysis/Election_Results.txt', 'w')
f.write('Election Results')
f.write('\n')
f.write('-----------------------------------------------')
f.write('\n')
f.write('\n')
print("Total Votes: " + str(number_votes), file=f) # 4. https://blog.enterprisedna.co/python-write-to-file/
f.write('\n')
f.write('-----------------------------------------------')
f.write('\n')
f.write('\n')

# Dynamically print candidate name, % of votes and # votes
for i in range(number_candidates):
    print(f'{uniq_candidates_list[i]}: {list(dict_pct.values())[i]}% ({list(dict_count.values())[i]})', file=f)
    f.write('\n')

f.write('-----------------------------------------------')
f.write('\n')
f.write('\n')
print(f'Winner: {winner_name}', file=f)
f.write('\n')
f.write('-----------------------------------------------')
f.close()