import json
def getsysdata(jsonFile):
    with open(jsonFile, 'r') as sysData:
        system = json.load(sysData)

    dnac = system['sandbox']
    #username = dnac['username']
    #password = dnac['password']
    #url = dnac['baseUrl']
    return dnac

if __name__=='__main__':
    from sys import argv
    import json
    function, file = argv
    dnac = getsysdata(file)
    print(dnac)

