import _help
import _cities
import _scale

readme = "/readme.txt"
sh_readme = False
#SEE THE COMMENTS BELOW

city = int(input("""
Please select one of theese cities:
  
1: San salvador
2: Quito
3: Medellín
4: Provide your own data
5: Instructions
  
  """))

#+++++++++++++++++++++++++++++++++++++++
#Setting the city
#+++++++++++++++++++++++++++++++++++++++
if city == 1:
    _cities.san_esa.sort()
    c_aq = _cities.san_esa
elif city == 2:
    _cities.qu_ec.sort()
    c_aq = _cities.qu_ec
elif city == 3:
    _cities.med_co.sort()
    c_aq = _cities.med_co
elif city == 4:
    c_aqp = int(input("""
What is usually the air quality on your city?
  """))
elif city == 5:
    sh_readme = True
    c_aqp = 0
#+++++++++++++++++++++++++++++++++++++++


if city <= 3:
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

  c_aqp = (c_aq[0]+c_aq[len(c_aq)-1]+c_aqm)/3

  #||||||||||||||||||||||||||||||||||||||||
else:
  print()
  # To use information given by the user

if sh_readme == False:
  _scale.scale(c_aqp)
else:
  print(open("ztxtz/readme.txt", "r").read())

print("""



""")

helpp = input("""

Show help (y/n) """)

if helpp == "y":
  _help.help(c_aqp)

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