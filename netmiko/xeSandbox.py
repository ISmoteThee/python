from netmiko import ConnectHandler

xeRtr = {
    'device_type': 'cisco_ios',
    'host': 'sandbox-iosxe-latest-1.cisco.com',
    'username': 'developer',
    'password': 'C1sco12345',
    'port': 22
}

conection = ConnectHandler(**xeRtr)
if conection.is_alive():
  print(f"{xeRtr['host']} is connected")
output = conection.send_command('show ip int br')
print(output)