import csv
import random
from os.path import expanduser
path = expanduser('~/Library/Application Support/Out of the Park Developments/OOTP Baseball 21/saved_games/SB.lg/import_export/draft.csv')
with open(path, 'r') as f:
    reader = csv.reader(f)
    teams = [(row[3],row[4]) for row in reader if row[0] == '2']

order = []
for n in range(0,10):
    if n == 0 :
        order.extend([[1,0,i+1,row[0],row[1],0,''] for i,row in enumerate(random.sample(teams,k=12))])
    elif n%2 == 0 :
        order.extend([ [n+1,0,i+1,row[0],row[1],0,''] for i,row in enumerate(teams[::-1])])
    else :
        order.extend([ [n+1,0,i+1,row[0],row[1],0,''] for i,row in enumerate(teams)])

with open(path, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['//Format: Draft Round','Supplemental (1 = yes or 0 = no)',	 'Pick in Round',	 'Team Name',	 'Team ID',	 'Player ID'])
    writer.writerows(order)
