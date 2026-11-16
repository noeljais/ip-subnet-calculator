import ipaddress
try:

   ip=input("Enter IP address with CIDR : ")
   result=ipaddress.ip_network(ip,strict=False)
   print("Network Address : ",result.network_address)
   print("Subnet Mask : ",result.netmask)
   print("Broadcast Address : ",result.broadcast_address)
   print("Total Address : ",result.num_addresses)
   print("Usable Hosts : ",result.num_addresses-2)
except ValueError:
    print("Invalid Input...try entering correct IP Address")