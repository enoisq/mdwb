import psutil

mac_addresses = []

nics = psutil.net_if_addrs()
#nics.pop('lo') # remove loopback since it doesnt have a real mac address

for i in nics:
    for j in nics[i]:
        mac_addresses.append(j.address)

print (mac_addresses[0])
