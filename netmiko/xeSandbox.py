from netmiko import ConnectHandler

xeRtr = {
    'device_type': 'cisco_ios',
    'host': 'ios-xe-mgmt.cisco.com',
    'username': 'developer',
    'password': 'C1sco12345',
    'port': 8181
}

# conection = ConnectHandler(**xeRtr)
# conection.send_command('show ip int br')