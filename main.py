#SEE THE COMMENTS BELOW

san_esa = [88,111,84,62,63,61,61,50,46,53,75,87,72,56,44,133,152,151,151,95,94,94,82,88,121,145,130,105,150,135,159,162,137,136,114,110,132,137,150,132,101,137,140,151,155,75,128,95,96,97,136,143,110,110,127,134,99,94,103,110,113,126,144,103,148,83,104,114,127,113,124,152,152,156,162,43,60,49,54,53,54,47,49,51,50,51,63,64,59,57,55,53,56,63,59,82,95,107,107,95,96,107,120,148,152,139,157,102,94,78,86,82,68,57,63,69,68,67,69,59,55,58,62,82,72,74,56,60,56,60,77,69,61,67,66,56,45,60]

qu_ec = [59,55,46,56,64,77,72,67,70,54,52,74,71,76,69,56,63,62,69,81,81,62,48,74,57,67,62,46,56,79,75,56,60,61,71,74,73,70,61,81,70,62,77,56,59,81,65,36,46,49,43,43,43,54,52,50,32,79,53,49,66,50,38,39,55,49,53,64,57,35,46,45,36,37,55,54,49,55,58,62,69,42,42,68,62,74,58,70,67,69,43,63,60,40,57,78,70,80,81,69,46,53,45,26,40,33,26,41,24]

med_co = [63,59,57,67,60,56,57,62,59,67,76,85,71,62,70,70,60,82,69,59,56,55,53,57,55,58,59,68,67,72,85,89,65,65,55,53,62,69,85,93,65,64,61,78,89,81,61,62,56,53,60,58,62,77,77,95,60,23,56,55,56,63,67,61,56,58,63,61,76,60,58,54,69,90,43,44,43,55,73,72,70,75,66,48,54,57,55,56,60,53,59,59,52,58,62,65,53,46,68,72,81,61,51,57,55,55,58,58,56,46,41,53,57,57,58,59,45,48,52,56,57,52,46,49,41,44,44,53,58,66,68,60,57,75,59,67]

usc_uslnd = []

city = int(input("""
Please select one of theese cities:
  
1: San salvador
2: Quito
3: Medellín
4: Provide your own data
  
  """))

#+++++++++++++++++++++++++++++++++++++++
#Setting the city
#+++++++++++++++++++++++++++++++++++++++
if city == 1:
  san_esa.sort()
  c_aq = san_esa
elif city == 2:
  qu_ec.sort()
  c_aq = qu_ec
elif city == 3:
  med_co.sort()
  c_aq = med_co
else:
  usc_uslnd.append(int(input("""
What is usually the air quality on your city?
  """)))
#+++++++++++++++++++++++++++++++++++++++


if city != 4:
  #////////////////////////////////////////
  #Median:
  #////////////////////////////////////////
  #||| If len(c_aq) is odd

  if round(len(c_aq)/2)-(len(c_aq)/2) != 0:
    c_aqm = c_aq[int(( len(c_aq) / 2) - 0.5)]

  #||| If len(c_aq) is even
  else:
    v1 = c_aq[int(len(c_aq)/2)]
    v2 = c_aq[int(len(c_aq)/2)+1]
  
    c_aqm = (v1+v2)/2
  #////////////////////////////////////////



  #||||||||||||||||||||||||||||||||||||||||
  #The final results:
  #||||||||||||||||||||||||||||||||||||||||

  c_aqp = (c_aq[0]+c_aq[len(c_aq)-1]+c_aqm)/2

  #||||||||||||||||||||||||||||||||||||||||
elif city == 4:
  c_aqp = usc_uslnd[0]
  # To use information given by the user
else:
  print("")

if c_aqp >= 300:
  print("""
The air quality in this city is very dangerous, and living there can decrease your lifetime considerably (https://aqicn.org/scale/en/)""")
elif c_aqp >= 201:
  print("""
The air quality in this place can be hazardous for anyone (https://aqicn.org/scale/en/)""")
elif c_aqp >= 151:
  print("""
The air quality in this place can be unhealthy (https://aqicn.org/scale/en/)""")
elif c_aqp >= 101:
  print("""
The air quality in this place con be hazardous for sensitive groups (https://aqicn.org/scale/en/)""")
elif c_aqp >= 51:
  print("""
The air quality in this place is acceptable, but a very small group of people could be affected (https://aqicn.org/scale/en/)""")
else:
  print("""
The air quality in this place is good (https://aqicn.org/scale/en/)""")

#------------------------------------
#Variables
#------------------------------------

# c_aq is a list ([1,2,3,4,5...]) filled with the
# infomation collected in the last months of everyday's
# air quality in the selected city

# c_aqm is the median from all these values organized from
# lowest to highest

# c_aqp is the sum of the lowest value from the list, the
# highest value, and the median, divided by three

# The median is needed for knowing if there are more high
# values than low values, and giving a more accurate
# average