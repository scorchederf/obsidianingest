import os,sys,argparse
from datetime import datetime
import logging
import subprocess


#EMAIL
from smtplib import SMTP
from email import encoders
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

#KEYVAULT
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

#ZIP
import zipfile

#region "Logging"
# Adopted from https://stackoverflow.com/a/35804945/1691778
# Adds a new logging method to the logging module
def addLoggingLevel(levelName, levelNum, methodName=None):
    if not methodName:
        methodName = levelName.lower()

    if hasattr(logging, levelName):
        raise AttributeError("{} already defined in logging module".format(levelName))
    if hasattr(logging, methodName):
        raise AttributeError("{} already defined in logging module".format(methodName))
    if hasattr(logging.getLoggerClass(), methodName):
        raise AttributeError("{} already defined in logger class".format(methodName))

    def logForLevel(self, message, *args, **kwargs):
        if self.isEnabledFor(levelNum):
            self._log(levelNum, message, args, **kwargs)

    def logToRoot(message, *args, **kwargs):
        logging.log(levelNum, message, *args, **kwargs)

    logging.addLevelName(levelNum, levelName)
    setattr(logging, levelName, levelNum)
    setattr(logging.getLoggerClass(), methodName, logForLevel)
    setattr(logging, methodName, logToRoot)

# addLoggingLevel("GOOD", logging.INFO - 5)
level    = logging.INFO
format   = '%(asctime)s %(levelname)-8s %(message)s'
dtefmt   = '%Y-%m-%d %H:%M:%S'
dtestamp = datetime.today().strftime('%Y%m%d')
logfile  =  os.path.join("c:\\git", "cyber", "team", "adam", "logging", dtestamp + "-stub.log")
handlers = [logging.FileHandler(logfile), logging.StreamHandler()]
logging.basicConfig(level = level, format = format, handlers = handlers, datefmt=dtefmt)

logging.debug("debug level logging")    # DEBUG: For debugging purposes in development
logging.info("this informational")      # INFO: This level is used when something expected happens, such as opening a new session
logging.warning("this is a warning")    # WARNING: This level is used when something unexpected or unusual happens. A warning is not an error but requires attention.
logging.error("this is an error")       # ERROR: This level is for things that go wrong but are usually recoverable
logging.critical("Critical message")    # CRITICAL: Use this level in a doomsday scenario.

# this shoudl only be used in a 
# try:
#   print('')
# except Exception as e:
#   logging.exception("Exception occurred")


#endregion

#   2023-03-22T23:19:05     '%Y-%m-%dT%H:%M:%S'
timestamp = datetime.today().strftime('%Y-%m-%dT%H:%M:%S')
#   print(timestamp)

def GetKeySecret(key_name):
    try:
      os.environ.setdefault('AZURE_USERNAME', 'SVC_INT_CYBERTSK_PRD@int.ucq.com.au')
      credentials = DefaultAzureCredential( additionally_allowed_tenants=['*'] )
      vault_name = "prd-ae-security"
      secret_client = SecretClient(vault_url=f"https://{vault_name}.vault.azure.net/", credential=credentials)
      secret = secret_client.get_secret(key_name)
      key_secret= secret.value
      return key_secret.split(':')
    except Exception as ex:
      print("GetKeyVault Exception :", ex)
#key, secret = GetKeySecret("APIkey-FalconReadonly")


dir_path = os.path.join("c:\\git", "cyber", "templates", "Attachments")
# if the files variable exists, the items in the array will be attached
attachments = ['How to change your password.pdf', 'Self Service Password Reset_User Guide_v6.0.pdf']
def send_email(to_email, message_txt, html_txt):
    try:
        print("sending email")
        msg = MIMEMultipart("alternative")          #
        msg['Subject'] = "Email subject"
        msg['From'] = "cyber@ucareqld.com.au"
        msg['To'] = to_email
        msg.attach(MIMEText(message_txt, "plain"))
        msg.attach(MIMEText(html_txt, "html"))
        if 'attachments' in globals():
            #print('variable named files exits')
            for f in attachments:
                filepath = os.path.join(dir_path, f)
                with open(filepath, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())    
                    encoders.encode_base64(part) # Encode file in ASCII characters to send by email    
                    part.add_header("Content-Disposition", f"attachment; filename= {f}",) # Add header as key/value pair to attachment part
                    msg.attach(part) # Add attachment to message and convert message to string
        with SMTP('mail') as smtp:      
            smtp.send_message(msg)              # send email

    except Exception as ex:
      print("send_email Exception :", ex)
#send_email("adam.stein@ucareqld.com.au","plaintxt for the win","<html><head></head><body><font color='green'>hiya team</font></body></html>")



def BackupKeyVault():
  try:
    os.environ.setdefault('AZURE_USERNAME', 'SVC_INT_CYBERTSK_PRD@int.ucq.com.au')
    credentials = DefaultAzureCredential( additionally_allowed_tenants=['*'] )
    vault_name = "prd-ae-security"
    secret_client = SecretClient(vault_url=f"https://{vault_name}.vault.azure.net/", credential=credentials)
    #secret = secret_client.get_secret(key_name)
    secret_properties = secret_client.list_properties_of_secrets()

    with zipfile.ZipFile("keyvault.zip", mode="w") as archive:
      #archive.setpassword("secret")
      with archive.open("data.csv", "w") as data:
        header = "name,value,version,contenttype,id,\r\n"
        data.write(bytes(header, encoding='utf8'))
        for secret_property in secret_properties:
          # the list doesn't include values or versions of the secrets
          #print(secret_property.name)
          secret = secret_client.get_secret(secret_property.name)
          #print(secret.name)

          line = ("\"" + str(secret.name) + "\"" + "," + 
             "\"" + str(secret.value) + "\""+ "," +
             "\"" + str(secret.properties.version) + "\"" + "," +
             "\"" + str(secret.properties.tags) + "\"" + "," +
             "\"" + str(secret.properties.content_type) + "\"" + "," +
             "\"" + str(secret.properties.id) + "\"" + "," +
             "\r\n"
             )
          #print (line)
          data.write(bytes(line, encoding='utf8'))

    child = subprocess.Popen('"C:\\Program Files\\7-Zip\\7z.exe" a -t7z c:\\git\\cyber\\kv.7z c:\\git\\cyber\\keyvault.zip -ppizzaisawesome -sdel', shell=False)
    streamdata = child.communicate()[0]
    rc = child.returncode 

    #key_secret= secret.value

    #return key_secret.split(':')
  except Exception as e:
    print(sys.exc_info())
    #print("GetKeyVault Exception :", ex.with_traceback)

#BackupKeyVault()


def ZipFileStream():
  with zipfile.ZipFile("hello.zip", mode="w") as archive:
    #archive.setpassword(b"secret")
    #archive.write("hello.txt")
    with archive.open("data.txt", "w") as new_hello:
      new_hello.write(b"Hello, World!")

#ZipFileStream()





#region MainFunction
#When a python program is executed, python interpreter starts executing code inside it. It also sets few implicit variable values, one of them is __name__ whose value is set as __main__.

#For python main function, we have to define a function and then use if __name__ == '__main__' condition to execute this function.

#If the python source file is imported as module, python interpreter sets the __name__ value to module name, so the if condition will return false and main method will not be executed.

def main():
    print("hello world!")
    # Setting arguments for input of critical Variables
    parser = argparse.ArgumentParser()

    parser.add_argument("-s","--superstring",help="a string parameter", required=True, default="I am a string")
    args = parser.parse_args()
    logging.info(args.superstring)


if __name__ == "__main__":
    main()


#endregion

