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
  #temp_ids.append(temp_id) 
  #temp_names.append(temp_name) 
  
#print temp_ids 
#print temp_names 

#Load in seeds and IDs from TourneySeeds.csv
seedfile = open("TourneySeeds.csv") 
for line in seedfile: 
  line = line[:-1].split(',')
  seed = line[1] 
  idnumber = line[2] 
  if line[0] != "2017": continue  
  seeds.append(seed)
  x = 0 
  for id_ in temp_id: 
    if id_ == idnumber: names.append(temp_names[i]) 
    print id_ 
    print idnumber 
    #x += 1  
  ids.append(idnumber[:-1])
  #ids.append(idnumber[:-1]) 
  #if idnumber_ in temp_ids: 
    #print temp_id 


print seeds 
print ids
print names 
