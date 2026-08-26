import re
import datetime
f = open("C:\\dev\\git\\bravo\\offsec\\web100\\exam\\flag2.input", "r")
lines = f.readlines()
f.close()

for i in range(0, len(lines)):
  lines[i] = lines[i][:-1] #Remove trailing newline character

myans = ""
for l in lines:
  pattern = re.compile("\d{4}year-INPUT-(0?[1-9]|1[012])month-(2[0-3]|[01]?[0-9])hour-([0-5][0-9])second-([0-3][0-9])day-TIMESTAMP-[0-5][0-9]minute, Data: .") #Implement the correct regular expression to ensure that the timestamp fits the correct syntactic format.
  if pattern.match(l): #If the line matches the pattern
    #print (l)
    # Implement your semantic checks here on the remaining timestamps
    #   YYYYyear-INPUT-MMmonth-HHhour-sssecond-DDday-TIMESTAMP-mmminute, Data: c
    #   \d{4}year-INPUT-(0?[1-9]|1[012])month-(2[0-3]|[01]?[0-9])hour-([0-5][0-9])second-([0-3][0-9])day-TIMESTAMP-[0-5][0-9]minute, Data: .
    # 
    # [0-5][0-9]minute-TIMESTAMP---INPUT--
    #print (l)
    try:
      dteitem = l.split("-")
      iyear =     int(dteitem[0].replace("year", ""))
      #INPUT
      imonth =    int(dteitem[2].replace("month", ""))
      ihour =     int(dteitem[3].replace("hour", ""))
      isecond =   int(dteitem[4].replace("second", ""))
      iday =      int(dteitem[5].replace("day", ""))        #last field needs to be split again
      #TIMESTAMP
      iminute =   int((dteitem[7].replace("minute", "")).split(",")[0])
      d = datetime.datetime(iyear, imonth, iday, ihour, iminute, isecond)
      #print (d)
      #print('Valid date string')
      ans = dteitem[7].replace("day", "").split(",")[1].replace("Data: ", "")
      myans += ans
    except ValueError:
        err = 1
        print('Invalid date string')

print(myans.replace(" ", ""))



































'''


import re
import datetime



lines = f.readlines()
f.close()

for i in range(0, len(lines)):
  lines[i] = lines[i][:-1] #Remove trailing newline character

response = ""
for l in lines:
  pattern = re.compile("") #Implement the correct regular expression to ensure that the timestamp fits the correct syntactic format.
  if pattern.match(l): #If the line matches the pattern
    # Implement your semantic checks here on the remaining timestamps
    #   0       - 1      - 2       - 3     - 4    - 5   - 6      - 7
    #   2019year-17minute-TIMESTAMP-10month-15hour-INPUT-56second-05day
    try:
        dteitem = l.split("-")
        iyear =     int(dteitem[0].replace("year", ""))
        imonth =    int(dteitem[2].replace("month", ""))
        iday =      int(dteitem[5].replace("day", ""))        #last field needs to be split again
        ihour =     int(dteitem[3].replace("hour", ""))
        iminute =   int(dteitem[7].replace("minute", ""))
        isecond =   int(dteitem[4].replace("second", "")).split(",")[0]
        d = datetime.datetime(iyear, imonth, iday, ihour, iminute, isecond)
        #print('Valid date string')
        ans = dteitem[7].replace("day", "").split(",")[1].replace("Data: ", "")
        response += ans
    except ValueError:
        err = 1
        #print('Invalid date string')

print(response.replace(" ", ""))

'''