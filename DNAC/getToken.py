import requests
from requests.auth import HTTPBasicAuth
import json
from getSysData import getsysdata

def getToken(dnac):
    
    url = f"{dnac['baseUrl']}/dna/system/api/v1/auth/token"
    payload={}

    response = requests.post(url, auth=HTTPBasicAuth(dnac['username'], dnac['password']))
    jsonResponse = json.loads(response.text)
    token = jsonResponse['Token']
    return token

if __name__=='__main__':
    dnac = getsysdata('dnac.json')
    print(getToken(dnac))


