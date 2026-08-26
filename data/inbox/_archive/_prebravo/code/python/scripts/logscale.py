
import datetime
import logging
from logging import Formatter, Handler
import sys
import time
import requests
import json


falconurl = "https://ucareqld.ingest.logscale.us-2.crowdstrike.com/api/v1/ingest/hec"
falconheaders = ({
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 3cbe5629-f35a-4b9d-b09b-b96811569aed'
})
filelogpath = "c:\\temp\\test.log"
dtefmt   = '%Y%m%dT%H:%M:%SZ'
format = json.dumps({
        'time': '%(asctime)s',
        'pathname': '%(pathname)s',
        'line': '%(lineno)d',
        'logLevel': '%(levelname)s',
        'message': '%(message)s'
})


class HTTPPostHandler(logging.Handler):
    def __init__(self, url: str, source: str, host: str):
        super().__init__()
        self.url = url
        self.source = source
        self.host = host

    def emit(self, record):
        log_entry = self.format(record)
        headers = { "Content-Type": "text/plain; charset=utf-8","Authorization": "Bearer 3cbe5629-f35a-4b9d-b09b-b96811569aed"}
        msg=None
        try:
            #try converting to json, if fails ASSume it is a plain string
            msg = json.loads(record.message.replace("'", "\""))
        except:
            msg = {
                "desc": record.message 
            }
        msg["loglevel"] = record.levelname
        try:
            customdata = {
                "time":     int(time.time()),
                "source":   self.source,
                "host":     self.host,
                "event":    msg
            }
            #print(customdata)
            response = requests.post(self.url, json=customdata, headers=headers, stream=True)
            #print (response.text)
            response.raise_for_status()
        except Exception as e:
            print("Unexpected error:", sys.exc_info()[0])


logging.basicConfig(level=logging.INFO)
http_endpoint_url = falconurl
http_handler = HTTPPostHandler(url=falconurl, source="test1-py", host="localdevice")
logging.getLogger('').addHandler(http_handler)

#logging.info('{"time": 1690260210, "source": "adamtest.py", "host": "localmachine", "event":"hi"}')
logginginfo = {
                    "desc":"successfully retrieved azure keyvault secret",
                    "vault":"Test-1-ShouldBeAvailable",
                    "booo":"NOTICE"
                }  
logging.info({"desc":"hello", "data":"123"})

logging.info("this is ok")
logging.error("its bad")
logging.warning("alarm alarm")
logging.info(logginginfo)