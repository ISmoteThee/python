from netmiko import ConnectHandler

xrRtr = {
    'device_type': 'cisco_xr',
    'host': 'sbx-iosxr-mgmt.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'port': 8181
}

# conection = ConnectHandler(**xrRtr)
# conection.send_command('show ip int br')