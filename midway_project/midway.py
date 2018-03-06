import argparse

def parse_args(): 
  ap = argparse.ArgumentParser() 
  ap.add_argument("-m", "--mode", type=str, default = "default", choices = ["states", "regions", "coords"], help="Choose mode: states, regions, or coords.") 
  #ap.add_argmument("-s", "--search", type=str, choices
  args = vars(ap.parse_args()) 
  return args

print "Welcome to American Cities from W to R."
filename = "cities.csv"
citydata = open(filename, 'r') 

def state_searcher(): 
  state = raw_input("State: ")
  for x in citydata: 
    if state in x: 
      stuff = x.split(', ')
      print stuff[8].strip('"')
    elif state not in x:
      continue
  print "|* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|"
  print "| * * * * * * * * *  :::::::::::::::::::::::::|"
  print "|* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|"
  print "| * * * * * * * * *  :::::::::::::::::::::::::|"
  print "|* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|"
  print "| * * * * * * * * *  ::::::::::::::::::::;::::|"
  print "|* * * * * * * * * * OOOOOOOOOOOOOOOOOOOOOOOOO|"
  print "|:::::::::::::::::::::::::::::::::::::::::::::|"
  print "|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|"
  print "|:::::::::::::::::::::::::::::::::::::::::::::|"
  print "|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|"
  print "|:::::::::::::::::::::::::::::::::::::::::::::|"
  print "|OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO|"



def region_searcher():
  #citydata = open(filename, 'r') 
  
  Northeast = ["CT", "ME", "MA", "NH", "RI", "VT", "NJ", "NY", "PA"]
  New_England = ["CT", "ME", "MA", "NH", "RI", "VT"]
  Mid_Atlantic = ["NJ", "NY", "PA"]
  East_North_Central = ["IL", "IN", "MI", "OH", "WI"]
  West_North_Central = ["IA", "KS", "MN", "MO", "NE", "ND", "SD"]
  Midwest = ["IL", "IN", "MI", "OH", "WI", "IA", "KS", "MN", "MO", "NE", "ND", "SD"]
  South_Atlantic = ["DE", "FL", "GA", "MD", "NC", "SC", "VI", "DC", "WV"]
  East_South_Central = ["AL", "KY", "MS", "TN"]
  West_South_Central = ["AR", "LA", "OK", "TX"]
  South = ["DE", "FL", "GA", "MD", "NC", "SC", "VI", "DC", "WV", "AL", "KY", "MS", "TN", "AR", "LA", "OK", "TX"]
  Mountain = ["AZ", "CO", "ID", "MT", "NV", "NM", "UT", "WY"]
  Pacific = ["AK", "CA", "HI", "OR", "WA"]
  West = ["AZ", "CO", "ID", "MT", "NV", "NM", "UT", "WY", "AK", "CA", "HI", "OR", "WA"]
  
  region = raw_input("Region: ") 
  
  for x in citydata: 
    filelinecomponents = x.split(', ') 
    if region == "Northeast" or region == "northeast" or region == "north east" or region == "north-east" or region == "North-east": 
      matched_region = Northeast
    elif region == "New England" or region == "new england" or region == "New england": 
      matched_region = New_England
    elif region == "Mid-Atlantic" or region == "Mid Atlantic" or region == "mid atlantic" or region == "midatlantic" or region == "Midatlantic" or region == "mid-atlantic": 
      matched_region = Mid_Atlantic
    elif region == "East North Central" or region == "East north central" or region == "east north central":
      matched_region = East_North_Central 
    elif region == "West North Central" or region == "West north central" or region == "west north central":
      matched_region = West_North_Central
    elif region == "Midwest" or region == "midwest" or region == "mid-west" or region == "Mid-west" or region == "mid west":
      matched_region = Midwest 
    elif region == "South Atlantic" or region == "South atlantic" or region == "south atlantic":
      matched_region = South_Atlantic 
    elif region == "East South Central" or region == "east south central" or region == "East south central":
      matched_region = East_South_Central 
    elif region == "West South Central" or region == "West south central" or region == "west south central":
      matched_region = West_South_Central
    elif region == "South" or region == "the South" or region == "the south" or region == "The South" or region == "south":
      matched_region = South 
    elif region == "Mountain" or region == "mountain" or region == "Mountain region" or region == "mountain region":
      matched_region = Mountain 
    elif region == "Pacific" or region == "pacific" or region == "Pacific region" or region == "pacific region":
      matched_region = Pacific  
    else:
      print "Region not recognized. Please try again."
      break
    for i in range(len(matched_region)): 
      if matched_region[i] in filelinecomponents[9]:
        print filelinecomponents[8].strip('"')     
      elif matched_region[i] not in x: 
        continue   

def degr2dec(d, m, s): 
  dd = d + float(m)/60 + float(s)/3600
  return dd 

def compass_searcher(): 
  user_input = raw_input("Latitude, longitude: ") 
  LatLong = user_input.split(', ')
  UserLat = float(LatLong[0])
  UserLong = float(LatLong[1])
  
  print "Here are all the American R-W cities northeast of your coordinates:"
  lineno = -1
  for x in citydata: 
    lineno += 1
    if lineno == 0: 
      continue
    filelinecomponents = x.split(', ') 
    LatCord = degr2dec(int(filelinecomponents[0]), int(filelinecomponents[1]), int(filelinecomponents[2])) 
    #print LatCord
    LongCord = degr2dec(int(filelinecomponents[4]), int(filelinecomponents[5]), int(filelinecomponents[6]))  
    City = filelinecomponents[8].strip('"')
    State = filelinecomponents[9].strip('"')[:-1] 
    if 'LatD' in filelinecomponents[1]:
      continue
    #elif 'LatD' not in filelinecomponents[1]: 
      #print LatCord  
    elif LatCord > UserLat and LongCord < UserLong:
      print City, State
      continue 
    elif LatCord > UserLat and LongCord >= UserLong:
      continue
    elif LatCord <= UserLat:
      continue 
    else: 
      print "What?" 
      break


def ask_user(): 
  print "Please select mode:"
  user_input = raw_input("Type S to search cities by state, Type R to search by region, Type C to search by coordinates: ") 
  if user_input.lower() == "s":
    state_searcher() 
  if user_input.lower() == "r":
    region_searcher()
  if user_input.lower() == "c":
    compass_searcher()
    
args = parse_args()   
if args["mode"].lower() == "states":
  state_searcher() 
if args["mode"].lower() == "regions":
  region_searcher()
if args["mode"].lower() == "coords":
  compass_searcher()
if args["mode"].lower() == "default": 
  ask_user() 

