import sys, os
import pandas as pd
import requests
import logging, datetime, time
import csv

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

logfile  = os.path.join("c:\\dev\\batchlogscale\\", datetime.datetime.today().strftime('%Y%m%d') + "-" + (os.path.basename(__file__).replace(".py", ".log")))
initLogging(logfile, logging.INFO)


API_TOKEN = "6SHK5eJBGQKh8PtcjAbHakDJ~KVeUuVRj0YfxNyErOMPbKIxluqyBGdSRU2HhgPx8zVRY"
postUrl = "https://ucareqld.logscale.us-2.crowdstrike.com/api/v1/repositories/ucqv-overview/query" 

headers = {
    'Authorization': f"Bearer {API_TOKEN}",
    'Accept': 'application/x-ndjson'
}

ruleNames = [
    "Guest_BYOD_ISE_Portal_Apps"
    ,"724_Downtime_Mid Tier_Rule"
    ,"BYOD_Outbound_INet_Ports"
    ,"BYOD_to_MedicalSuites_All"
    ,"Management_DD_Mgmt_In_Apps"
    ,"UCH Citrix to Siemens Server Access_Allow"
    ,"From_SCCMPS_incoming"
    ,"RFC_to_SCCMDP"
    ,"UCH_to_UCQ_New_citrix_farm"
    ,"Managed_UC_MitelContr_Apps.2"
    ,"724_Downtime_Mid Tier_Rule"
    ,"724_Downtime_RDP_Rule"
    ,"EPO Test1"
    ,"To_SCCMDP_outgoing"
    ,"UCH_Mitel_MCD_to_UCH_VMCD Communications"
    ,"UCH_Mitel_AX_Contoller_to_UCH_MCD_VMCD Communications"
    ,"UCH_Mitel_VMCD_MCD_to_UCH_VMBG Communications"
    ,"UCH_Mitel_IP_Phone_to_UCH_VMCD"
    ,"UCH_Mitel_IP_Phone_to_UCH_VMBG"
    ,"UCH_MCD_VMCD AXController Micolab to Mitel License"
    ,"Mitel IP Trunks Mitel BPH AX Controller to UCH MCD-VMCD"
    ,"Mitel UCC_Teleworkers Communication"
    ,"To_SCCMMP_outgoing"
    ,"From Foetal networks to DB"
    ,"From Citrix_Svr to DB-1"
    ,"From Foetal MonitorWS to Web"
    ,"Biomed_Printing_Foetal"
    ,"From Foetal Anthena clients"
    ,"Foetal_Portal_Printing_access"
    ,"Equitrac-Upgrade"
    ,"Biomed_RDP_in_Foetal-1"
    ,"Guest_BYOD_ISE_Portal_Apps"
    ,"BYOD_Printing_Apps"
    ,"BYOD_Outbound_Medi-Object-App"
    ,"BYOD_Outbound_INet_Apps"
    ,"BYOD_Outbound_INet_Ports"
    ,"Med_Suites_Dr_Larwood_vpn"
    ,"UHC_Domain_Controller_AD_Remedian"
    ,"Critical_alert_trigger"
    ,"Management_AllowMgmtSyslog"
    ,"Management_DD_Mgmt_In_Apps-2"
    ,"VMaaS_Vulnerability_Scan_INT"
    ,"UCQ_ServiceNow_Discovery"
    ,"Management_To_ISE_Apps"
    ,"Management_DD_Mgmt_Out_Apps"
    ,"Management_To_3p_WLC_Auth_Apps"
    ,"Management_WLC_Anchor_Apps"
    ,"Management_WLC_Anchor_Apps-1-Secured"
    ,"Management_WLC_Licensing_Apps"
    ,"Management_From_ISECoA_Ports"
    ,"Management_ISEPAN_PSN_Ports"
    ,"Management_AllowMgmt_Apps"
    ,"Med_Suites_Inbound_INetVMO_Apps"
    ,"Med_Suites_Inbound_Inet_Apps.3"
    ,"Med_Suites_Inbound_Inet_Apps.4"
    ,"Med_Suites_Inbound_INet_DrBogdn"
    ,"Biomed_DHCP_Apps"
    ,"Biomed_DNS_Apps"
    ,"Biomed_TopCat_Wifi_Ports.1"
    ,"Biomed_TopCat_Wifi_Ports"
    ,"Biomed_TopCat_Wifi_Apps"
    ,"Biomed_Ekahau_Server_Ports"
    ,"Biomed_Camera Stacks_In_Apps"
    ,"Biomed_Camera Stacks_In_Ports"
    ,"Biomed_Camera Stacks_Out_Ports"
    ,"Biomed_Camera Stacks_Out_Apps"
    ,"Biomed_Alaris_IVPumps_Ports"
    ,"Biomed_AD_Apps"
    ,"Biomed_AD_Apps1"
    ,"Biomed_SCCM_Apps"
    ,"Biomed_SCCM_apps_out-1"
    ,"TEG Analyzer API Port to Server"
    ,"TEG Mgr Srvr Analyzer API Port"
    ,"MACLAB ACS to API_SMB_MLCL_MSSQL"
    ,"MACLAB ACS to ADDC"
    ,"MACLAB_ACS_GEHealthcare_Insite"
    ,"MACLAB API_SMB_MLCL_MSSQL to ACS"
    ,"Biomed_XlCelera_Apps.1"
    ,"Biomed_Printing_Apps.1"
    ,"Biomed_CCL_ToSiemes_Apps"
    ,"Biomed_CCL_ToSiemens_Ports"
    ,"Biomed_Siemens_ToCCL_Apps"
    ,"Biomed_Siemens_ToCCL_Ports"
    ,"Biomed_XlCelera_In_Apps"
    ,"Imprivata_VNC_Remote_access_to_BPH_WyseTerminal"
    ,"Biomed_PACS_Philips_Ports"
    ,"UCQ_ISCV_Browsing"
    ,"Biomed_PACS_Servers_Ports"
    ,"Arthrex_Access"
    ,"Intellispace_server_out"
    ,"Intellispace_server_in"
    ,"Biomed_XFer_Test.1"
    ,"Kronos_Internet_Apps_Out"
    ,"Kronos_Internet_Apps_Out-1"
    ,"Managed_Zone_UCH_Clients-ssl"
    ,"Managed_Zone_UCH_Clients"
    ,"SAMserver_To_Snow"
    ,"Management_TSCPH_AD_Apps.2"
    ,"Management DHCP rule"
    ,"Managed_DNS_Apps"
    ,"Managed_TSCPH_AD_Apps.1"
    ,"Managed_Corp_In_Webdav_Apps"
    ,"Management_DNS_In_Apps"
    ,"Managed_TSCPH_AD_Apps.2"
    ,"Thinclient_Cloud_WMS_Communication"
    ,"Managed_Printing_EPP_Apps"
    ,"Managed_Printing_In_Apps"
    ,"Managed_Printing_In_Apps.3"
    ,"Managed_Printing_In_SAP_Apps"
    ,"Managed_Printing_In_Ports"
    ,"Managed_UC_PolyCom_AV_Apps.2-1"
    ,"Managed_UC_PolyCom_AV_Apps.1-1"
    ,"Managed_UC_AscomVoIP_Apps.1"
    ,"Managed_UC_AV_Apps.2"
    ,"Managed_UC_MitelVoIPRTP_Ports"
    ,"Managed_UC_MitelContr_Apps.1"
    ,"Managed_UC_MitelContr_Ports.1"
    ,"Managed_Mitel_Ports.2"
    ,"Managed_UC_MitelVoIP_Apps"
    ,"Managed_UC_PolyCom_NTP_Apps"
    ,"Managed_TSCPH_Hicaps devices"
    ,"Managed_UC_PolyCom_DNS_Apps"
    ,"UCQ-DNAC_Incoming_Access_Allowed"
    ,"UCQ-DNAC_Incoming_Access_Allowed-Non_std"
    ,"UCQ-DNAC_Outgoing_Access_Allowed"
    ,"UCQ-DNAC_Outgoing_Access_Allowed-Non_std"



#THIS IS HUGE, DONE MANUALLY
#   ,"UCH_Proxy_internet"

]


# get a list of completed rules so we dont double up and redownload processed items
excludedRules = os.listdir("C:\\dev\\batchlogscale\\completed\\")


doDownload = True
doConversion = True


for ruleName in ruleNames:
    tmpfilename = f"C:\\dev\\batchlogscale\\{ruleName}.tmp"


    if (doDownload):
        # DOWNLOAD SECTION
        if (f"{ruleName}.csv" in excludedRules):
            logging.info(f"{ruleName} already processed")
            continue
        logging.info(f"{ruleName} starting")

                    #'queryString': f'#repo=ucq-palofirewall | Type=TRAFFIC | in(field=domain, values=["TSCPH-CORE-FW-P003", "TSCPH-CORE-FW-P004"]) | RuleName = "{ruleName}"',
        jsonData = {
            'queryString': f'#repo=ucq-palofirewall | Type=TRAFFIC | in(field=domain, values=["TSCPH-CORE-FW-P003", "TSCPH-CORE-FW-P004"]) | RuleName = "{ruleName}" | groupBy(field=[SourceZone, SourceIP, DestinationZone, DestinationIP, NATSourceIP, NATDestinationIP, Application, DestinationPort, Protocol])',
            'start': '60d',
            'isLive': False,
        }
        with requests.post(postUrl, headers=headers, json=jsonData, stream=True) as r:
            r.raise_for_status()
            with open(tmpfilename, 'wb', buffering=1000) as f:           # buffering set to 1mb
                count = 1
                print("downloading - start")
                for chunk in r.iter_content(chunk_size=None): 
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    if chunk: 
                        if (count % 1000 == 0):
                            #print("*", end=" ")
                            print('*', end='', flush=True)
                        count += 1
                        #logging.debug(f"{ruleName} chunk written")
                        f.write(chunk)
                print("")
                print("downloading - finished")
            logging.info(f"{ruleName} request returned {r.status_code}")
        time.sleep(5)

    if (doConversion):
        if os.path.isfile(tmpfilename):
            logging.info(f"{ruleName} have a file to process")
            outfilename = f"C:\\dev\\batchlogscale\\completed\\{ruleName}.csv"
            CHUNKSIZE = 10000
            ##FIELDNAMES = ("#error","#humioAutoShard","#repo","#type","@collect.host","@collect.id","@collect.remote","@collect.socket","@collect.source_name","@collect.source_type","@collect.timestamp","@collect.timezone","@error","@error_msg","@error_msg[0]","@id","@ingesttimestamp","@rawstring","@timestamp","@timestamp.nanos","@timezone","Action","Application","ApplicationCategory","ApplicationSubCategory","BytesReceived","BytesSent","BytesTotal","Category","DestinationIP","DestinationPort","DestinationUser","DestinationZone","NATDestinationIP","NATDestinationPort","NATSourceIP","NATSourcePort","Protocol","ReceiveTime","RuleName","SerialNumber","SessionID","SourceIP","SourcePort","SourceUser","SourceZone","StartTime","Type","_fu1","csv_data","domain","sysLogDateTime")
            FIELDNAMES = ("SourceZone", "SourceIP", "DestinationZone", "DestinationIP", "NATSourceIP", "NATDestinationIP", "Application", "DestinationPort", "Protocol", "_count")
            isFirst = True
            with open(outfilename, "a+") as fout:
                logging.info(f"{ruleName} header written")
                for df in pd.read_json(tmpfilename, chunksize=CHUNKSIZE, lines=True):
                    if (isFirst):
                        df.to_csv(outfilename, mode='a+', header=True)
                        logging.info(f"{ruleName} writing csv chunk with header")
                        isFirst = False
                    else:
                        df.to_csv(outfilename, mode='a+', header=False)
                        logging.info(f"{ruleName} writing csv chunk")





# https://www.reddit.com/r/dataengineering/comments/eyugsd/how_to_convert_a_big_json_file_to_csv_format/
def convertjsontocsv():
        #logging.info(f"{ruleName} returned {l} results")
        df = pd.read_json(tmpfilename)
        logging.info(f"{ruleName} temp file contains {len(df.index)} records")
        #df = pd.DataFrame.from_dict(j)
        df.to_csv(f"C:\\dev\\batchlogscale\\completed\\{ruleName}.csv")
        logging.info(f"{ruleName} saved to csv, sleeping for 5")



