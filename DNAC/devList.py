import requests
import json
from sys import argv
from getToken import getToken
from getSysData import getsysdata

file = 'dnac.json'
#if argv[1]:
#    file = argv[1]
dnac = getsysdata(file)


url = dnac['baseUrl'] + "/dna/intent/api/v1/network-device"

payload={}
headers = {
  'X-Auth-Token': getToken(dnac)
}

response = requests.request("GET", url, headers=headers, data=payload)
dict_resp = json.loads(response.text)
devices = dict_resp['response']
i = 1
for device in devices:
    print(f"-----Device {i}:  {device['hostname']}-----")
    print(f"Type: {device['series']}")
    print(f"IP Address:  {device['managementIpAddress']}")
    print()
    i += 1




