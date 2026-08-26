import importlib.util
from optparse import OptionParser
import sys, os, logging, csv
import argparse
import requests, json
from datetime import datetime, timedelta
from falconpy import APIHarness
import pandas as pd
import subprocess

# region "DO NOT DELETE - import common functions, init logging"
spec = importlib.util.spec_from_file_location("inc", "C:\\git\\cyber\\scheduledtasks\\inc.py")
inc = importlib.util.module_from_spec(spec)
sys.modules["inc"] = inc
spec.loader.exec_module(inc)

logfile = os.path.join("c:\\temp\\", datetime.today().strftime('%Y%m%d') + "-" + (os.path.basename(__file__).replace(".py", ".log")))
inc.initLogging(logfile, logging.INFO)
# endregion

def sendNotifications(msg):
    logging.info("about to start sending notifications")
    html = msg
    body = html.format()
    inc.sendmail("cyber@ucareqld.com.au", emailFrom, emailSubject, body)     #;vidya.jadhav@ucareqld.com.au



def getToken(last_token=None, last_token_time=None):
    # Let's configure the authorization request with the necessary data
    authurl = csfUrl + '/oauth2/token'
    auth_headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    authdata = {
        "client_id": clientId,
        "client_secret": clientSecret
    }

    if last_token_time and last_token:
        delta = datetime.utcnow() - last_token_time
        # Check if our token is older than 25 min
        if (delta.total_seconds() / 60) <= 15:
            logging.debug("Auth Token still good")
            return last_token, last_token_time
        else:
            logging.info("Refreshing Auth Token: {}".format((str(datetime.utcnow().strftime('%Y_%m_%d %H-%M-%S')))))
    # Get & decode bearer token
    r = requests.post(authurl, headers=auth_headers, params=authdata)
    token_time = datetime.utcnow()
    auth_string = r.content.decode('utf8')
    json_auth = json.loads(auth_string)
    try:
        bearer = json_auth['access_token']
    except KeyError as e:
        logging.critical(
            "Received a KeyError for the 'access_token': ".format(r))
        exit(0)
    # Setup the header for future requests
    idp_header = {
        "Authorization": "Bearer " + bearer,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    return idp_header, token_time

def saveCursor(end_cursor):
    logging.debug("Cursor file: {}".format(cursorFile))
    with open(cursorFile, 'a+', encoding='UTF8', newline='') as f:
        f.write(f'{end_cursor}\n')

def queryData(runQuery):
    # Setup the IDP URL
    idp_url = csfUrl + "/identity-protection/combined/graphql/v1"

    initial_token, initial_token_time = getToken()

    if not endCursor_global:
        r = requests.post(idp_url, headers=initial_token, json={'query': runQuery})
    else:
        variables = {}
        variables['after'] = endCursor_global
        r = requests.post(idp_url, headers=initial_token, json={'query': runQuery, 'variables': variables})

    results = json.loads(r.content.decode('utf-8'))
    logging.debug(results)


    data = results['data']
    entities = data['entities']
    nodes = entities['nodes']

    spnClone = spnBaseline.copy()


    for n in nodes:
      disp = n['secondaryDisplayName']
      if disp == "QLD.BLUECARE.ORG.AU\\svc_0032------TEST":     # test to trigger non removal and new items
        csSpn = disp
      else:
        csSpn = disp.lower()
      
      
      if csSpn in spnClone:
          logging.info("removing " + csSpn)
          spnClone.remove(csSpn)
      else:
          
          logging.info("appending " + csSpn)
          spnClone.append("[NEW] " + csSpn)

    
    msg = "<b>This is a work in progress and part of the AD hardening project by our most awesome Mel!</b><br><br>"
    msg += "The items below were either added or not removed to the SPNBaseline. <br>NEW items means they have extra permissions, EXISTING items should have been removed."

    if len(spnClone) > 0:
        msg += "<table>"
        for spn in spnClone:
            if spn.startswith("[NEW] "): 
                msg += ("<tr><td>NEW</td><td>" + spn.replace("[NEW] ", "") + "</td></tr>")
            else:
                msg += ("<tr><td>EXISTING</td><td>" + spn + "</td></tr>")
        msg += "</table>"
    sendNotifications(msg)



              
            
            

#this is our baseline
spnBaseline = ["lccq.org.au\\svc_0010","qld.bluecare.org.au\\svc_0036","qld.bluecare.org.au\\svc_0101","uhc.uc.com.au\\svc_0045","uhc.uc.com.au\\prdadm","qld.bluecare.org.au\\sqlservice","uhc.uc.com.au\\sqlc01_d002_svc","qld.bluecare.org.au\\svc_0042","qld.bluecare.org.au\\svc_0070","int.ucq.com.au\\svc_0001","lccq.org.au\\svc_0011","int.ucq.com.au\\svc_0010","uhc.uc.com.au\\prod_bc_proxy","qld.bluecare.org.au\\svc_0039","qld.bluecare.org.au\\svc_0066","uhc.uc.com.au\\svc_uhc_sauboe_prd","qld.bluecare.org.au\\svc_0041","qld.bluecare.org.au\\svc_uatprophix","int.ucq.com.au\\svc_int_cybertsk_prd","qld.bluecare.org.au\\svc_0109","uhc.uc.com.au\\svc_sqlc02prodsvc","uhc.uc.com.au\\sqlc01_d001_svc","lccq.org.au\\svc_0008","lccq.org.au\\svc_0009","qld.bluecare.org.au\\svc_0013","qld.bluecare.org.au\\sql_svcprocura01","uhc.uc.com.au\\svc_uhc_sqlc01_prd","qld.bluecare.org.au\\svc_0032","qld.bluecare.org.au\\sql_svcmicroster","uhc.uc.com.au\\svc_infosec","qld.bluecare.org.au\\svc_0150","int.ucq.com.au\\sqlexec","qld.bluecare.org.au\\svc_0065","uhc.uc.com.au\\sqlman","uhc.uc.com.au\\sqlservices_durin","int.ucq.com.au\\svc_infosec"]

emailFrom = "cyber@ucareqld.com.au"
emailSubject = "[ALERT] SPN CHECK"

csfUrl = "https://api.us-2.crowdstrike.com"
clientId, clientSecret = inc.GetKeySecret("APIkey-FalconHostTag")
csvFile = os.path.join("c:\\temp\\", datetime.today().strftime('%Y%m%d') + "-" + (os.path.basename(__file__).replace(".py", ".csv")))
cursorFile = os.path.splitext(csvFile)[0] + ".txt"
endCursor_global = ""
# qryCount = """{countEntities(types: [USER], dataSources: [ACTIVE_DIRECTORY], hasWeakPassword: true, roles: [AdminAccountRole], archived: false, enabled: true)}"""
qryBase = """
                # To list all the users with SPNs:
                {
                    entities(
                        types: [USER]
                        first: 1000
                        riskFactorTypes: [HAS_SPNS]
                    )
                    {
                        nodes
                        {
                            primaryDisplayName
                            secondaryDisplayName
                            isHuman: hasRole(type: HumanUserAccountRole)
                            isProgrammatic: hasRole(type: ProgrammaticUserAccountRole)
                            isPrivileged: hasRole(type: AdminAccountRole)
                        }
                    }
}

"""


def main():
    qry = qryBase
    #logging.info("Query: {}".format(qry))
    queryData(qry)


if __name__ == '__main__':
    main()
