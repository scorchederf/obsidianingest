import os,sys,argparse
from datetime import datetime
import logging
from logging import Formatter, Handler
import requests
from logging.handlers import HTTPHandler
from requests.adapters import HTTPAdapter
import inspect
from functools import partial, partialmethod
import json
import time
import subprocess

#AZURE
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

#MAIL
from smtplib import SMTP
from email import encoders
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from urllib3 import Retry


""" Logging 

#region "import common functions, init logging"
import importlib
spec = importlib.util.spec_from_file_location("inc", "C:\\secops\\git\\cyber\\common\\inc.py")
inc = importlib.util.module_from_spec(spec)
sys.modules["inc"] = inc
spec.loader.exec_module(inc)
logfile  = datetime.today().strftime('%Y%m%d') + "-" + (os.path.basename(__file__).replace(".py", ".log"))
inc.initLogging(logfile, logging.INFO)
#endregion

"""
#custom level NOTICE = 25
logpath = "c:\\temp"
smtpserver = "mail.uchealth.com.au"

class HTTPPostHandler(logging.Handler):
    def __init__(self, url: str, source: str, host: str, logscaletoken: str):
        super().__init__()
        self.url = url
        self.source = source
        self.host = host
        self.logscaletoken = logscaletoken

    def emit(self, record):
        log_entry = self.format(record)
        headers = { "Content-Type": "text/plain; charset=utf-8","Authorization": "Bearer {0}".format(self.logscaletoken)}
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







def initLogging(logfile, loglevel, hostname, scriptname, logscaletoken = "3cbe5629-f35a-4b9d-b09b-b96811569aed"):

    #disable extra logging on azure http
    logger = logging.getLogger("azure.core.pipeline.policies.http_logging_policy")
    logger.setLevel(logging.WARNING)

    #new custom level for success
    logging.NOTICE = 25
    logging.addLevelName(logging.NOTICE, 'NOTICE')
    logging.Logger.notice = partialmethod(logging.Logger.log, logging.NOTICE)
    logging.notice = partial(logging.log, logging.NOTICE)

    fulllogfile = logpath + "\\" + logfile
    daystamp = datetime.today().strftime('%Y%m%d')
    format   = "%(asctime)s {} {} LOG - %(levelname)s - %(message)s".format(hostname, scriptname) # %(scriptname)s LOG - %(levelname)s - %(message)s"
    #format = logging.Formatter(json.dumps({
    #    'time': '%(asctime)s',
    #    'pathname': '%(pathname)s',
    #    'line': '%(lineno)d',
    #    'logLevel': '%(levelname)s',
    #    'message': '%(message)s'
    #}))
    #   '%(asctime)s %(levelname)-8s %(message)s'    # %(name)s: is useful for debugging as it shows the module name
    dtefmt   = '%Y%m%dT%H:%M:%SZ'           #    '%Y-%m-%d %H:%M:%S'



    falconurl = "https://ucareqld.ingest.logscale.us-2.crowdstrike.com/api/v1/ingest/hec"
    logscaleHandler = HTTPPostHandler(url=falconurl, source=scriptname, host=hostname, logscaletoken=logscaletoken)

    handlers = [logging.FileHandler(fulllogfile), logging.StreamHandler(), logscaleHandler]
    logging.basicConfig(level = loglevel, format = format, handlers = handlers, datefmt=dtefmt)
    logging.debug("hello world")




def GetLogFilePath(logfile):
    return logpath + "\\" + logfile

    

""" return a file contents 
Example usage

print(readFile("C:\\git\\cyber\\templates\\WeakPasswords.html"))
"""
def readFile(filepath):
    with open(filepath, 'r') as f:
        lines = f.read()
    return lines

""" Sending email
Example usage

attachments=[logfile, logfile]
htmlbody = helper.readFile("C:\\git\\cyber\\templates\\WeakPasswords.html")
helper.sendmail("adam.steinucareqld.com.au", "cyberautomation@ucareqld.com.au", "This is a test", htmlbody, attachments)

"""
def sendmail(mailto, mailfrom, subject, body, attachments=None):
    try:
        logging.debug(inspect.getargvalues(inspect.currentframe())) 
        msg = MIMEMultipart("alternative")          #
        msg['Subject'] = subject
        msg['From'] = mailfrom
        msg['To'] = mailto
        msg['Bcc'] = "adam.stein@ucareqld.com.au"
        msg['X-Priority'] = '2'
        #msg.attach(MIMEText(message_txt, "plain"))
        msg.attach(MIMEText(body, "html"))
        if attachments is not None:
            for f in attachments:
                with open(f, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())    
                    encoders.encode_base64(part) # Encode file in ASCII characters to send by email    
                    part.add_header("Content-Disposition", f"attachment; filename= {os.path.basename(f)}",) # Add header as key/value pair to attachment part
                    msg.attach(part) # Add attachment to message and convert message to string
        #with SMTP(smtpserver) as smtp:      
        #    smtp.send_message(msg)              # send email
        log = {}
        log["desc"] = "sent email"
        log["to"] = mailto
        log["subject"] = subject
        log["from"] = mailfrom
        
        logging.debug(json.dumps(log))
    except Exception as ex:
      logging.error("SendMail exception: ", ex)


"""Azure KeyVault
Example usage

key, secret = GetKeySecret("APIkey-FalconReadonly")

"""
def GetKeySecret(key_name):
    try:
      os.environ.setdefault('AZURE_USERNAME', 'SVC_INT_CYBERTSK_PRD@int.ucq.com.au')
      credentials = DefaultAzureCredential( additionally_allowed_tenants=['*'] )
      vault_name = "prd-ae-security"
      logging.getLogger("azure.core.pipeline.policies.http_logging_policy").setLevel(logging.WARN)
      secret_client = SecretClient(vault_url=f"https://{vault_name}.vault.azure.net/", credential=credentials)
      secret = secret_client.get_secret(key_name)
      key_secret= secret.value
      logging.debug("retrieved {}".format(key_name))
      return key_secret.split(':')
    except Exception as ex:
      logging.exception("GetKeyVault Exception :", ex)



def GetKeySecret2(token):
	executable = r'C:\Program Files\BitwardenCLI\bws.exe'  # Use a raw string to avoid escape characters
	arguments = ['-t', os.environ["BWS_ACCESS_TOKEN"], 'secret', 'get', token]
	try:
		result = subprocess.run([executable] + arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
		data = json.loads(result.stdout)
		logging.debug("retrieved {}".format(token))
		return data['value']
	except Exception as ex:
		logging.exception("Get Bitwarden Secrets manager exception :", ex)