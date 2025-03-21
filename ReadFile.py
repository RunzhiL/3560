#!/user/bin/env python3

ip_file = open("ips.txt","r")

ip_address = ip_file.read()
print(ip_address)

ip_file.close()