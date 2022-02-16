from sys import argv

script, prefix, maskLength = argv
hostIp = input(f"\nAssigned network is {prefix}/{maskLength}\n" + \
                "What host ip should I set? " )

print(f"OK, host ip is {hostIp} on network {prefix}/{maskLength}.\n")
print(f"Finished with script {script}")
print(f"Values in argv list: {argv}\n")
