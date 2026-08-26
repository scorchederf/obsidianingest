import re

f = open("C:\\dev\\git\\bravo\\offsec\\web100\\attempt1\\flag.input", "r")
lines = f.readlines()
f.close()

for i in range(0, len(lines)):
  lines[i] = lines[i][:-1] #Remove trailing newline character

mypattern = "\d{4}year-[0-5][0-9]minute-TIMESTAMP-(0?[1-9]|1[012])month-(2[0-3]|[01]?[0-9])hour-INPUT-([0-5][0-9])second-([0-3][0-9])day"

for l in lines:
  pattern = re.compile(mypattern) #Implement the correct regular expression to ensure that the timestamp fits the correct syntactic format.
  if pattern.match(l): #If the line matches the pattern
    # Implement your semantic checks here on the remaining timestamps
    print(l)

