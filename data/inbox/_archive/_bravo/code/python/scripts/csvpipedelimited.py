import csv
import datetime
import zoneinfo
import pytz

#epoch = datetime.datetime.utcfromtimestamp(0)
def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0



filepath = "C:\\dev\\dbcyph0n\\bravo\\code\\python\\scripts\\query.csv"
startDate = datetime.datetime(2024,2,6)
zone = pytz.timezone("Australia/Brisbane")
au = zone.localize(datetime.datetime(2024,2,6), is_dst=None)




#autime = tz.localize(startDate)
#epochStartDate = autime
#print(epochStartDate.strftime('%S'))
#print(zoneinfo.available_timezones())




qrybase = """
#repo=ucq-palofirewall
| domain = "TSCPH-CORE-FW-*"
| cidr(SourceIP, subnet=[{src}]) 
| cidr(DestinationIP, subnet=[{dst}])
| in(Application, values=[{app}])
"""




with open(filepath, 'r') as file:
  csvreader = csv.reader(file, delimiter="|", quotechar=None)
  for row in csvreader:
    src = row[0]
    dst = row[1]
    app = row[2]
    qry = qrybase.format(src=src,dst=dst,app=app)
    print(qry)

