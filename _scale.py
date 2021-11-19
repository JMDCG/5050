def scale(c_aqp):
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