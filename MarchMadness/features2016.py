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
  if line[0] != "2016": continue  
  seed = line[1] 
  seeds.append(seed)
  i = 0 
  for id_ in temp_ids: 
    if id_ == idnumber: names.append(temp_names[i]) 
    i += 1  
  ids.append(idnumber)

print "These are the seeds from 2016: ", seeds 
print "These are IDs for the 2016 teams: ", ids
print "These are the names corresponding to the above 2016 IDs: ", names

#Declare more variables! 
winteams = []
loseteams = [] 
winteams_names = []
loseteams_names = []
pts1 = []
pts2 = []
wfgms = []
wfgas = []
lfgms = []
lfgas = []
n3ptrs1 = []
n3ptrsa1 = []
n3ptrs2 = []
n3ptrsa2 = []
wftms = []
wftas = []
lftms = [] 
lftas = []
wors = []
wdrs = []
lors = []
ldrs = []
wasts = []
lasts = []
wtos = []
ltos = []
wstls = []
lstls = []
wblks = []
lblks = []
wpfs = []
lpfs = []

#Load in the 2016 game details from RegularSeasonCompactResults.csv
season2016compfile = open("RegularSeasonCompactResults.csv") 
for line in season2016compfile: 
  line = line[:-1].split(',') 
  if line[0] != "2016": continue  
  winteam = line[2] 
  winteams.append(winteam) 
  loseteam = line[4] 
  loseteams.append(loseteam) 
  pt1 = line[3] 
  pts1.append(int(pt1)) 
  pt2 = line[5] 
  pts2.append(int(pt2)) 

#Load in the 2016 game details from RegularSeasonDetailedResults.csv 
season2016deatsfile = open("RegularSeasonDetailedResults.csv") 
for line in season2016deatsfile: 
  line = line[:-1].split(',') 
  if line[0] != "2016": continue 
  n3ptr1 = line[10] 
  n3ptrs1.append(int(n3ptr1)) 
  n3ptr2 = line[23] 
  n3ptrs2.append(int(n3ptr2)) 
  wfgm = line[8]
  wfgms.append(int(wfgm))
  lfgm = line[21]  
  lfgms.append(int(lfgm))
  wfga = line[9]
  wfgas.append(int(wfga))
  lfga = line[22] 
  lfgas.append(int(lfga))
  wor = line[14] 
  wors.append(int(wor))
  wdr = line[15] 
  wdrs.append(int(wdr))
  lor = line[27]
  lors.append(int(lor))
  ldr = line[28]
  ldrs.append(int(ldr))
  wast = line[16]
  wasts.append(int(wast))
  last = line[29]
  lasts.append(int(last))
  wto = line[17]
  wtos.append(int(wto))
  lto = line[30]
  ltos.append(int(lto))
  wstl = line[18]
  wstls.append(int(wstl))
  lstl = line[31]
  lstls.append(int(lstl))
  wblk = line[19]
  wblks.append(int(wblk))
  lblk = line[32]
  lblks.append(int(lblk))
  wpf = line[20]
  wpfs.append(int(wpf))
  lpf = line[33]
  lpfs.append(int(lpf))
  n3ptra1 = line[11]
  n3ptrsa1.append(int(n3ptra1))
  n3ptra2 = line[24]
  n3ptrsa2.append(int(n3ptra2))  
 

#Sync up names to ids in the winteams and loseteams lists
season2016compfile = open("RegularSeasonCompactResults.csv") 
for line in season2016compfile: 
  line = line[:-1].split(',')
  if line[0] != "2016": continue  
  winningteam = line[2] 
  losingteam = line[4] 
  i = 0
  for id2 in temp_ids: 
    if id2 == winningteam: winteams_names.append(temp_names[i]) 
    if id2 == losingteam: loseteams_names.append(temp_names[i]) 
    i += 1 

output = open("dataoutput16.csv", "w") 
output.write("team id, npts per game, n3ptrs, nRebounds, margin of victory, competitiveness of conference, seed")


#print "2016 winning team by games (ID): ", winteams 
#print "2016 losing team by games (ID): ", loseteams 
#print "2016 winning team by game (names): ", winteams_names
#print "2016 losing team by games (names): ", loseteams_names 
#print "2016 winning points by game: ", pts1
#print "2016 losing points by game: ", pts2
#print "2016 field goals made by team 1(winning team): ", wfgms
#print "2016 field goals attempted by team 1(winning team): ", wfgas
#print "2016 field goals made by team 2(losing team): ", lfgms
#print "2016 field goals attempted by team 2(losing team): ", lfgas
#print "2016 number of 3-pointers made by winning team: ", n3ptrs1 
#print "2016 number of 3-pointers attempted by winning team: ", n3ptrsa1
#print "2016 number of 3-pointers made by losing team: ", n3ptrs2
#print "2016 number of 3-pointers attempted by losing team: ", n3ptrsa2
#print "2016 number of free throws made by team 1(winning team): ", wftms
#print "2016 number of free throws attempted by team 1(winning): ", wftas
#print "2016 number of free throws made by team 2(losing team): ", lftms
#print "2016 number of free throws attempted by team 2(losing): ", lftas
#print "2016 number of offensive rebounds by team 1(winning): ", wors
#print "2016 number of defensive rebounds by team 1(winning): ", wdrs
#print "2016 number of offensive rebounds by team 2(losing): ", lors
#print "2016 number of defensive rebounds by team 2(losing): ", ldrs 
#print "2016 number of assists by team 1(winning): ", wasts
#print "2016 number of assists by team 2(losing): ", lasts
#print "2016 number of turnovers by team 1(winning): ", wtos
#print "2016 number of turnovers by team 2(losing): ", ltos
#print "2016 number of steals by team 1(winning): ", wstls
#print "2016 number of steals by team 2(losing): ", lstls
#print "2016 number of blocks by team 1(win): ", wblks
#print "2016 number of blocks by team 2(lose): ", lblks
#print "2016 number of personal fouls by team 1(win): ", wpfs
#print "2016 number of personal fouls by team 2(lose): ", lpfs 
