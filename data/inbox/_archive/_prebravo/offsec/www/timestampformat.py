import re
import datetime

f = open("C:\\dev\\git\\bravo\\offsec\\www\\flag.input", "r")
lines = f.readlines()
f.close()

for i in range(0, len(lines)):
  lines[i] = lines[i][:-1] #Remove trailing newline character

for l in lines:
  pattern = re.compile("(0?[1-9]|1[012])month-[0-5][0-9]minute-TIMESTAMP-INPUT-([0-5][0-9])second-(2[0-3]|[01]?[0-9])hour-\d{4}year-([0-3][0-9])day") #Implement the correct regular expression to ensure that the timestamp fits the correct syntactic format.
  if pattern.match(l): #If the line matches the pattern
    # Implement your semantic checks here on the remaining timestamps
    #print (l)
    data = l.split("-")
    month = data[0].replace("month", "")
    minute = data[1].replace("minute", "")
    second = data[4].replace("second","")
    hour = data[5].replace("hour", "")
    year = data[6].replace("year", "")
    daytemp = data[7].replace("day", "").replace(", Data:", "")
    day = daytemp.split(" ")[0]
    d = daytemp.split(" ")[1]
    #print (day, " | ", d)
    #print (month, minute, second, hour, year, day, d )#, d)
    date_format = '%Y-%m-%d'
    try:
        date_string = year + "-" + month + "-" + day
        dateObject = datetime.datetime.strptime(date_string, date_format)
        #print(dateObject)
        print (d, end="")
    except ValueError:
        #print ("is valid")
        isvalid = False
