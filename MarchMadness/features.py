#Declare variables
ids = [] 
names = []
seeds = []

#Load in school names from Teams.csv
temp_ids = []
temp_names = []
namefile = open("Teams.csv")
for line in namefile:
  line = line[:-1].split(',') 
  temp_id = line[0]
  temp_name = line[1] 
  temp_ids.append(temp_id) 
  temp_names.append(temp_name) 

#Load in seeds and IDs from TourneySeeds.csv
seedfile = open("TourneySeeds.csv") 
for line in seedfile: 
  line = line[:-1].split(',')
  idnumber = line[2][:-1] 
  if line[0] != "2017": continue  
  seed = line[1] 
  seeds.append(seed)
  i = 0 
  for id_ in temp_ids: 
    if id_ == idnumber: names.append(temp_names[i]) 
    i += 1  
  ids.append(idnumber)

print "These are the seeds from 2017: ", seeds 
print "These are IDs for the 2017 teams: ", ids
print "These are the names corresponding to the above 2017 IDs: ", names

#Declare more variables! 
winteams = []
loseteams = [] 
winteams_names = []
loseteams_names = []
pts1 = []
pts2 = []
n3ptrs1 = []
n3ptrs2 = []

#Load in the 2017 game details from RegularSeasonCompactResults.csv
season2017compfile = open("RegularSeasonCompactResults.csv") 
for line in season2017compfile: 
  line = line[:-1].split(',') 
  if line[0] != "2017": continue  
  winteam = line[2] 
  winteams.append(winteam) 
  loseteam = line[4] 
  loseteams.append(loseteam) 
  pt1 = line[3] 
  pts1.append(pt1) 
  pt2 = line[5] 
  pts2.append(pt2) 

#Load in the 2017 game details from RegularSeasonDetailedResults.csv 
season2017deatsfile = open("RegularSeasonDetailedResults.csv") 
for line in season2017deatsfile: 
  line = line[:-1].split(',') 
  if line[0] != "2017": continue 
  n3ptr1 = line[10] 
  n3ptrs1.append(n3ptr1) 
  n3ptr2 = line[23] 
  n3ptrs2.append(n3ptr2) 

#Sync up names to ids in the winteams and loseteams lists
 

print "2017 winning team by games (ID): ", winteams 
print "2017 losing team by games (ID): ", loseteams 
print "2017 winning team by game (names): ", winteams_names
print "2017 losing team by games (ID): ", loseteams_names 
print "2017 winning points by game: ", pts1
print "2017 losing points by game: ", pts2
print "2017 number of 3-pointers by winning team: ", n3ptrs1 
print "2017 number of 3-pointers by losing team: ", n3ptrs2
