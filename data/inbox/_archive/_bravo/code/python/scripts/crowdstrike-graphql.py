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
def initLogging(logfile, loglevel):
    #format   = '%(asctime)s %(levelname)-8s %(name)s: %(message)s'
    format   = '%(asctime)s %(levelname)-8s %(message)s'    # %(name)s: is useful for debugging as it shows the module name
    dtefmt   = '%Y-%m-%d %H:%M:%S'
    handlers = [logging.FileHandler(logfile), logging.StreamHandler()]
    logging.basicConfig(level = loglevel, format = format, handlers = handlers, datefmt=dtefmt)


logfile = os.path.join("c:\\temp\\", datetime.today().strftime('%Y%m%d') + "-" + (os.path.basename(__file__).replace(".py", ".log")))
initLogging(logfile, logging.INFO)
# endregion




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
    global endCursor_global
    if os.path.isfile(csvFile) == False:
        with open(csvFile, 'w', encoding='UTF8', newline='') as f:
            logging.info(f"csvFile does not exist, creating: {csvFile}")
            # removing spaces in header to make it easier in sendnotifications
            # original csvHeader = ['Object SID', 'samAccountName', 'Domain', 'Secondary Display Name', 'Email', 'Password Change (UTC)', 'Account Creation Date (UTC)', 'Last Update Time (UTC)', 'Organizational Unit', 'Primary Display Name', 'Risk Score', 'isAdmin', 'isHuman', 'isProgrammatic']
            csvHeader = ['ObjectSID', 'samAccountName', 'Domain', 'SecondaryDisplayName', 'Email', 'PasswordChange', 'AccountCreationDate', 'LastUpdateTime', 'OrganizationalUnit', 'PrimaryDisplayName', 'RiskScore', 'isAdmin', 'isHuman', 'isProgrammatic']
            writer = csv.writer(f)
            writer.writerow(csvHeader)

    # Setup the IDP URL
    idp_url = csfUrl + "/identity-protection/combined/graphql/v1"

    initial_token, initial_token_time = getToken()
    r = requests.post(idp_url, headers=initial_token,json={'query': qryCount})
    results = json.loads(r.content.decode('utf-8'))
    data = results['data']
    entityCount = data['countEntities']
    logging.info("Beginning API queries now")

    if not endCursor_global:
        r = requests.post(idp_url, headers=initial_token, json={'query': runQuery})
    else:
        variables = {}
        variables['after'] = endCursor_global
        saveCursor(endCursor_global)
        r = requests.post(idp_url, headers=initial_token, json={'query': runQuery, 'variables': variables})

    results = json.loads(r.content.decode('utf-8'))
    logging.debug(results)

    paging = True
    with open(csvFile, 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        while paging:
            try:
                data = results['data']
                timeline = data['timeline']
                nodes = timeline['nodes']       
                logging.debug("found nodes: {}".format(len(nodes)))

                for n in nodes:
                    email = "" 
                    recentstring = ""
                    row = ([
                        n['entity']['accounts'][0]['objectSid'], 
                        n['entity']['accounts'][0]['samAccountName'], 
                        n['entity']['accounts'][0]['domain'],  
                        n['entity']['secondaryDisplayName'], 
                        email,  
                        n['timestamp'],  
                        n['entity']['creationTime'], 
                        recentstring, 
                        n['entity']['accounts'][0]['ou'], 
                        n['entity']['primaryDisplayName'], 
                        n['entity']['riskScoreSeverity'], 
                        n['entity']['isAdmin'], 
                        n['entity']['isHuman'], 
                        n['entity']['isProgrammatic'] 
                        ])
                    logging.debug(row)
                    writer.writerow(row)




                pageInfo = timeline['pageInfo']
                paging = pageInfo['hasNextPage']
                if paging:
                    logging.debug("paging: {}".format(paging))
                    endCursor = pageInfo['endCursor']
                    saveCursor(endCursor)
                    # This checks for and refreshes token if necessary
                    logging.debug("refreshing token if required")
                    initial_token, initial_token_time = getToken(initial_token, initial_token_time)
                    # Configure new query using the value of 'endCursor' from the last query
                    variables = {}
                    variables['after'] = endCursor
                    logging.info("Requesting more results with endCursor ending in: {}".format(endCursor[-6:]))
                    r = requests.post(idp_url, headers=initial_token, json={'query': runQuery, 'variables': variables})
                    results = json.loads(r.content.decode('utf-8'))
                    
                
                

            except Exception as ex:
                logging.error((ex))



csfUrl = "https://api.us-2.crowdstrike.com"
clientId, clientSecret = inc.GetKeySecret("APIkey-FalconHostTag")
csvFile = os.path.join("c:\\logs\\", datetime.today().strftime('%Y%m%d') + "-" + (os.path.basename(__file__).replace(".py", ".csv")))
cursorFile = os.path.splitext(csvFile)[0] + ".txt"
endCursor_global = ""
qryCount = """{countEntities(types: [USER], dataSources: [ACTIVE_DIRECTORY], hasWeakPassword: true, roles: [AdminAccountRole], archived: false, enabled: true)}"""
qryBase = """
         query ($after: Cursor) {
          timeline(sourceEntityQuery: {types: [USER,CLOUD_SERVICE],hasWeakPassword: true, roles: [AdminAccountRole]}, types: [PASSWORD_CHANGE], startTime: "P-%sD", first:1000, after: $after, sortOrder: DESCENDING) {
            nodes {
              timestamp
              eventType
              eventLabel
               ... on TimelineEntityEvent {
                entity {
                  ...MinimalEntityDescriptor
                  accounts {
                    dataSource
                    ... on ActiveDirectoryAccountDescriptor {
                      objectSid
                      samAccountName
                      domain
                      ou
                    }
                  }
                  
                }
              }
              ... on TimelineUserOnEndpointActivityEvent {
                endpointEntity {
                  ...MinimalEntityDescriptor
                }
              }
            }
            pageInfo {
              hasNextPage
              endCursor
            }
          }
        }
        
        fragment MinimalEntityDescriptor on Entity {
          entityId
          type
          primaryDisplayName
          secondaryDisplayName
          isAdmin: hasRole(type: AdminAccountRole)
          isHuman: hasRole(type: HumanUserAccountRole)
          isProgrammatic: hasRole(type: ProgrammaticUserAccountRole)
          ... on UserEntity {
            emailAddresses
            riskScoreSeverity
            creationTime
            mostRecentActivity
          }
        }
      """



def main():
    parser = OptionParser(usage="Usage: %prog [options]", version="%prog 4.0")
    parser.add_option("-D", "--days", dest="days_opt", default="30", help="Define how many days to query last password change (1-31 Days). Default: 1")
    parser.add_option("--cursor", dest="start_cursor", help="Starting Cursor")
    (options, args) = parser.parse_args()
    qry = qryBase % (str(options.days_opt))
    logging.info("Query: {}".format(qry))
    if options.start_cursor:
        endCursor_global = options.start_cursor
    queryData(qry)


if __name__ == '__main__':
    main()
