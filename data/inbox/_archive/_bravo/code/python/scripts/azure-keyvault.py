'''
---
hashtags: 
  - #python
  - #azure
  - #keyvault
  - #
---


Requires the Azure CLI - https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=powershell
$TLS12Protocol = [System.Net.SecurityProtocolType] 'Ssl3 , Tls12';[System.Net.ServicePointManager]::SecurityProtocol = $TLS12Protocol
$ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi; Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi /quiet'; rm .\AzureCLI.msi

Once installed, exec the below line to authenticate

az login

'''
import logging
import sys, os
from datetime import datetime
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

logger = logging.getLogger('azure-*') #logging for all azure-* libraries
logger.setLevel(logging.DEBUG)

#for scheduled tasks, redirect all output to a file so we can see what the heckin is going on
redirectOutputToFile = True
if (redirectOutputToFile == True):
    path = 'c:\\temp\\adam.txt'
    print("Redirecting output to", path)
    #a to append, w to write only
    sys.stdout = open(path, 'a')
    sys.stderr = open(path, 'a')
    sys.stdin = open(path, 'a')
    print("\n\n\n\n------------")

now = datetime.now()
print("New execution commenced at", now)
whoami=os.getlogin()
print("executing as:", whoami)
print("setting AZURE_USERNAME environment variable")
os.environ.setdefault('AZURE_USERNAME', 'SVC_INT_CYBERTSK_PRD@int.ucq.com.au')
os.environ.setdefault("AZURE_TENANT_ID", "789a41d4-4276-46cc-98f7-f78218cd89d8")
os.environ.setdefault("KEY_VAULT_NAME", "passwordsolution")


azUsername=os.environ.get('AZURE_USERNAME')
print("azUsername=", azUsername)

credential = DefaultAzureCredential( additionally_allowed_tenants=['*'] )


client = SecretClient(
    vault_url="https://passwordsolution.vault.azure.net/",
    credential=credential
)
print("testing running as svc account")

secret = client.get_secret("Test-1-ShouldBeAvailable")
print("the secret value is:", secret.value)

sys.stdout.flush()
sys.stderr.flush()
sys.stdin.flush()
