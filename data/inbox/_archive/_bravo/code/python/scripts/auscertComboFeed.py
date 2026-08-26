#!/usr/bin/env python3
import time
import json
import requests
import validators
from defang import defang
from tldextract import extract

URL = "https://www.auscert.org.au/api/v1/malurl/combo-7-txt/"
API_KEY = "****************************"

logscaletoken = "**********************"

falconurl = "https://ucareqld.ingest.logscale.us-2.crowdstrike.com/api/v1/ingest/hec"
headers = { "Content-Type": "text/plain; charset=utf-8","Authorization": "Bearer {0}".format(logscaletoken)}

result = requests.get(URL, headers={'API-Key': API_KEY})
iocs = result.text.splitlines()
for ioc in iocs:
    isValidUri = validators.url(ioc)        #is it valid
    defung = defang(ioc, colon=True, all_dots=True) #lets defang it
    tld = extract(ioc)  #get fqdn
    #print (tld.registered_domain)
    #print(defung)
    print("------------")
    auscertFormat = {
        "uri":  defung,
        "fqdn": tld.fqdn
    }
    customdata = {
        "time":     int(time.time()),
        "source":   "auscert-004",
        "host":     "cyber01",
        "event":    json.dumps(auscertFormat)
    }
    response = requests.post(falconurl, json=customdata, headers=headers, stream=True)


#
#if result.status_code == 200:
#   for line in result.content.decode():
#        print("-----------", line)