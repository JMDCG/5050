def help(aq_p):
  # In case of an explanation or any kind of help is      # needed

  q = int(input("""
What help do you need?
  
1: What is p.m. 2.5?
2: What can I do to improove the air quality in this city?
  
  """))

  if q == 1:
    print(open("ztxtz/explanation.txt", "r").read())