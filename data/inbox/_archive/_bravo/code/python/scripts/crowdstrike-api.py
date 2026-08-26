import requests
from falconpy import Intel






#curl -X POST "https://api.crowdstrike.com/oauth2/token" \
# -H "accept: application/json" \
# -H "Content-Type: application/x-www-form-urlencoded" \
# -d "client_id=a1b2c3d4e5f6&client_secret=QWE987RTY654UIOP321"


authUrl = "https://api.us-2.crowdstrike.com/oauth2/token"
authHeaders = { "Content-Type": "application/x-www-form-urlencoded","accept": "application/json"}

def csGet():
    clientid = "7af8bc2e85b047e1a9a18f9044f7faaf"
    clientsecret = "B8DJbrvy0Ta51Rp4SzgKq9I3EWL6GtZ7YMh2jXOC"
    authPayloadTemplate = "client_id={clientid}&client_secret={clientsecret}"
    authPayload = authPayloadTemplate.format(clientid=clientid, clientsecret=clientsecret)
    authResponse = requests.post(url=authUrl, headers=authHeaders, data=authPayload)
    authData = authResponse.json()
    accessToken = authData["access_token"]
    # do actual stuff
    apiHeaders = { "Content-Type": "application/json","Authorization": "Bearer {0}".format(accessToken)}
    apiUrl = "https://api.us-2.crowdstrike.com/intel/entities/rules-latest-files/v1"
    response = requests.get(url=apiUrl, headers=apiHeaders)
    print(response.text)




def test():
    # Do not hardcode API credentials!
    falcon = Intel(client_id="7af8bc2e85b047e1a9a18f9044f7faaf",
                client_secret="B8DJbrvy0Ta51Rp4SzgKq9I3EWL6GtZ7YMh2jXOC"
                )
    print("am I authenticated?", falcon.authenticated())
    save_file = "some_file.zip"
    response = falcon.GetLatestIntelRuleFile(type="common-event-format")
    print(response)



def alienvault():
    avUrl = "https://otx.alienvault.com/api/v1/pulses/subscribed?page="
    avHeaders = {
         "X-OTX-API-KEY": "caf194eb437f527718999e1d896911f1c165e325aa6bbf7e3a54348b228cb22b"
    }
    for i in range(1,2):
        response = requests.get(url=avUrl, headers=avHeaders)
        jdata = response.json()
        iocs = jdata["results"]
        for ioc in iocs:
            indicators = ioc['indicators']
            for j in indicators:
                iocType = (j['type']).lower()
                iocIndicator = j['indicator']
                iocCreated = j['created']
                print(iocCreated, iocType, iocIndicator)




def cstest():
    from falconpy import Intel
    # Do not hardcode API credentials! Yeah, I know... just testing.
    falcon = Intel(client_id="4e2a3c5126e04a32b745917415a76567", client_secret="Bm0gTesL8QNWVA4flU5IGd9qX3oFS6EuPx1HO72C")
    print("am I authenticated?", falcon.authenticated())
    save_file = "some_file.zip"
    response = falcon.GetLatestIntelRuleFile(type="common-event-format")
    print(response)

cstest()



