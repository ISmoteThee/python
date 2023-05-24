from netmiko import ConnectHandler

xrRtr = {
    'device_type': 'cisco_xr',
    'host': 'sbx-iosxr-mgmt.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'port': 80
}


if __name__ == "__main__":
  conection = ConnectHandler(**xrRtr)
  iPintStatus = conection.send_command('show ip int br | in Gig')
  print(iPintStatus)