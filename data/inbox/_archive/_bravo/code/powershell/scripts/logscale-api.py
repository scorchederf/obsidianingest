import sys, os
import pandas as pd
import requests
import logging, datetime, time
import csv
import datetime

""" Logging 
Example usage

logfile  = os.path.join("c:\\dev\\batchlogscale\\", datetime.today().strftime('%Y%m%d') + "-" + (os.path.basename(__file__).replace(".py", ".log")))
inc.initLogging(logfile, logging.INFO)
"""
def initLogging(logfile, loglevel):
    #format   = '%(asctime)s %(levelname)-8s %(name)s: %(message)s'
    format   = '%(asctime)s %(levelname)-8s %(message)s'    # %(name)s: is useful for debugging as it shows the module name
    dtefmt   = '%Y-%m-%d %H:%M:%S'
    handlers = [logging.FileHandler(logfile), logging.StreamHandler()]
    logging.basicConfig(level = loglevel, format = format, handlers = handlers, datefmt=dtefmt)

def download(qry):
        # DOWNLOAD SECTION
        #'queryString': f'#repo=ucq-palofirewall | Type=TRAFFIC | in(field=domain, values=["TSCPH-CORE-FW-P003", "TSCPH-CORE-FW-P004"]) | RuleName = "{ruleName}"',
        jsonData = {
            'queryString': f'{qry}',
            'start':    epochStart,
            'end':      epochEnd,
            'isLive': False,
        }
        logging.info("------------------------------------------------------")
        logging.info(jsonData)
        logging.info("------------------------------------------------------")
        #logging.info(row)
        #logging.info("------------------------------------------------------")
        with requests.post(postUrl, headers=headers, json=jsonData, stream=True) as r:
            r.raise_for_status()

            with open(tmpfilename, 'wb') as f:           # buffering set to 1mb
                count = 1
                print("downloading - start")
                for chunk in r.iter_content(chunk_size=None): 
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    #print(chunk)
                    if chunk: 
                        if (count % 100 == 0):
                            print("*", end=" ")
                            print('*', end='', flush=True)
                        count += 1
                        #logging.debug(f"{ruleName} chunk written")
                        f.write(chunk)
                print("")
                print("downloading - finished")
            #logging.info(f"csv line {counter} request returned {r.status_code}")
        time.sleep(5)


def convert():
    if os.path.isfile(tmpfilename):
       #logging.info(f"{nme} have a file to process")
        outfilename = f"C:\\temp\\batchlogscale\\all.csv"
        CHUNKSIZE = 10000
        ##FIELDNAMES = ("#error","#humioAutoShard","#repo","#type","@collect.host","@collect.id","@collect.remote","@collect.socket","@collect.source_name","@collect.source_type","@collect.timestamp","@collect.timezone","@error","@error_msg","@error_msg[0]","@id","@ingesttimestamp","@rawstring","@timestamp","@timestamp.nanos","@timezone","Action","Application","ApplicationCategory","ApplicationSubCategory","BytesReceived","BytesSent","BytesTotal","Category","DestinationIP","DestinationPort","DestinationUser","DestinationZone","NATDestinationIP","NATDestinationPort","NATSourceIP","NATSourcePort","Protocol","ReceiveTime","RuleName","SerialNumber","SessionID","SourceIP","SourcePort","SourceUser","SourceZone","StartTime","Type","_fu1","csv_data","domain","sysLogDateTime")
        FIELDNAMES = ("RuleName", "lastseen", "firstseen", "_count") # , "DestinationIP", "Application", "Count", "TotalBytesReceived", "TotalBytesSent")
        isFirst = True
        with open(outfilename, "a+") as fout:
            #logging.info(f"{nme} header written")
            for df in pd.read_json(tmpfilename, chunksize=CHUNKSIZE, lines=True):
                if (isFirst):
                    df.to_csv(outfilename, mode='a+', header=True)
                    #logging.info(f"{nme} writing csv chunk with header")
                    isFirst = False
                else:
                    df.to_csv(outfilename, mode='a+', header=False)
                    #logging.info(f"{nme} writing csv chunk")
                    
            #writer = csv.DictWriter(fout, fieldnames=FIELDNAMES)
            #writer.writeheader()

logfile  = os.path.join("c:\\temp\\batchlogscale\\", datetime.datetime.today().strftime('%Y%m%d') + "-" + (os.path.basename(__file__).replace(".py", ".log")))
initLogging(logfile, logging.INFO)


API_TOKEN = "6SHK5eJBGQKh8PtcjAbHakDJ~KVeUuVRj0YfxNyErOMPbKIxluqyBGdSRU2HhgPx8zVRY"
postUrl = "https://ucareqld.logscale.us-2.crowdstrike.com/api/v1/repositories/ucqv-overview/query" 

headers = {
    'Authorization': f"Bearer {API_TOKEN}",
    'Accept': 'application/x-ndjson'
}
#qrybase = '#repo=ucq-palofirewall | domain = "SSHB-CORE-FW-*" | cidr(SourceIP, subnet=[{src}]) | cidr(DestinationIP, subnet=[{dst}]) | in(Application, values=[{app}]) | groupby(field=[RuleName,SourceZone,SourceIP,DestinationZone,DestinationIP, DestinationPort,Application], function=[count(as=Count), sum(field=BytesReceived, as="TotalBytesReceived"), sum(field=BytesSent, as="TotalBytesSent")], limit=350000)'

# qrybase = '#repo=ucq-palofirewall | domain = "{domain}" | RuleName = "{rulename}" | groupby(field=[RuleName, SourceIP, DestinationIP, SourceZone, DestinationZone, Application, DestinationPort], limit=200000)'
qrybase = "#repo=ucq-palofirewall | domain = /int/i | groupBy([RuleName], limit=\"20000\", function=[max(field=@timestamp, as=lastseen), min(field=@timestamp, as=firstseen), count()]) | formatTime(format=\"%A %d %B %Y, %R\", as=\"lastseen\", field=lastseen, timezone=\"Australia/Brisbane\") | formatTime(format=\"%A %d %B %Y, %R\", as=\"firstseen\", field=firstseen, timezone=\"Australia/Brisbane\")"


filepath = "C:\\temp\\batchlogscale\\20240327-HospitalRules-Batch2.csv"

#           https://www.epochconverter.com/ but it is needed in milliseconds
epochStart =    1714521600000       # 1708005600000
                #1707141600000
epochEnd =      1725148800000       # 1708869599000



doDownload = True
doConversion = True




qry = qrybase       #.format(domain=domain, rulename=rulename)
tmpfilename = f"C:\\temp\\batchlogscale\\all.tmp"
download(qry)
convert()



"""

with open(filepath, 'r') as file:
  csvreader = csv.reader(file, delimiter=",", quotechar=None)
  next(csvreader, None) #skip first row
  counter = 0
  for row in csvreader:
    counter += 1
    #       Name|SourceIP|DestinationIP|Application
    domain = row[0]
    rulename = row[1]
    d = domain.split("-")
    nme = f'[{d[0]}] {rulename}' 
    app = None  #row[3]


    tmpfilename = f"C:\\temp\\hospitalsfirewall\\{nme}.tmp"
    if (doDownload):
        # DOWNLOAD SECTION



        qry = qrybase.format(domain=domain, rulename=rulename)

        #'queryString': f'#repo=ucq-palofirewall | Type=TRAFFIC | in(field=domain, values=["TSCPH-CORE-FW-P003", "TSCPH-CORE-FW-P004"]) | RuleName = "{ruleName}"',
        jsonData = {
            'queryString': f'{qry}',
            'start':    epochStart,
            'end':      epochEnd,
            'isLive': False,
        }
        logging.info("------------------------------------------------------")
        logging.info(jsonData)
        logging.info("------------------------------------------------------")
        logging.info(row)
        logging.info("------------------------------------------------------")
        with requests.post(postUrl, headers=headers, json=jsonData, stream=True) as r:
            r.raise_for_status()

            with open(tmpfilename, 'wb') as f:           # buffering set to 1mb
                count = 1
                print("downloading - start")
                for chunk in r.iter_content(chunk_size=None): 
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    #print(chunk)
                    if chunk: 
                        if (count % 100 == 0):
                            print("*", end=" ")
                            print('*', end='', flush=True)
                        count += 1
                        #logging.debug(f"{ruleName} chunk written")
                        f.write(chunk)
                print("")
                print("downloading - finished")
            logging.info(f"csv line {counter} request returned {r.status_code}")
        time.sleep(5)

    if (doConversion):
        if os.path.isfile(tmpfilename):
            logging.info(f"{nme} have a file to process")
            outfilename = f"C:\\temp\\hospitalsfirewall\\completed\\{nme}.csv"
            CHUNKSIZE = 10000
            ##FIELDNAMES = ("#error","#humioAutoShard","#repo","#type","@collect.host","@collect.id","@collect.remote","@collect.socket","@collect.source_name","@collect.source_type","@collect.timestamp","@collect.timezone","@error","@error_msg","@error_msg[0]","@id","@ingesttimestamp","@rawstring","@timestamp","@timestamp.nanos","@timezone","Action","Application","ApplicationCategory","ApplicationSubCategory","BytesReceived","BytesSent","BytesTotal","Category","DestinationIP","DestinationPort","DestinationUser","DestinationZone","NATDestinationIP","NATDestinationPort","NATSourceIP","NATSourcePort","Protocol","ReceiveTime","RuleName","SerialNumber","SessionID","SourceIP","SourcePort","SourceUser","SourceZone","StartTime","Type","_fu1","csv_data","domain","sysLogDateTime")
            FIELDNAMES = ("RuleName", "SourceZone", "SourceIP", "DestinationZone", "DestinationIP", "Application", "Count", "TotalBytesReceived", "TotalBytesSent")
            isFirst = True
            with open(outfilename, "a+") as fout:
                logging.info(f"{nme} header written")
                for df in pd.read_json(tmpfilename, chunksize=CHUNKSIZE, lines=True):
                    if (isFirst):
                        df.to_csv(outfilename, mode='a+', header=True)
                        logging.info(f"{nme} writing csv chunk with header")
                        isFirst = False
                    else:
                        df.to_csv(outfilename, mode='a+', header=False)
                        logging.info(f"{nme} writing csv chunk")
                     
                #writer = csv.DictWriter(fout, fieldnames=FIELDNAMES)
                #writer.writeheader()
"""



# https://www.reddit.com/r/dataengineering/comments/eyugsd/how_to_convert_a_big_json_file_to_csv_format/
#def convertjsontocsv():
#        #logging.info(f"{ruleName} returned {l} results")
#        df = pd.read_json(tmpfilename)
#        logging.info(f"{ruleName} temp file contains {len(df.index)} records")
#        #df = pd.DataFrame.from_dict(j)
#        df.to_csv(f"C:\\temp\\batchlogscale\\completed\\{ruleName}.csv")
#        logging.info(f"{ruleName} saved to csv, sleeping for 5")



