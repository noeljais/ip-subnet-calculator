import ipaddress

try:
    ip = input("Enter IP address with CIDR: ")
    result = ipaddress.ip_network(ip, strict=False)

    if result.version != 4 or result.prefixlen > 30:
        print("Please enter an IPv4 subnet with CIDR /0 to /30.")
    else:
        print("Network Address:", result.network_address)
        print("Subnet Mask:", result.netmask)
        print("Broadcast Address:", result.broadcast_address)
        print("Total Addresses:", result.num_addresses)
        print("Usable Hosts:", result.num_addresses - 2)
        print("First Usable IP:", result.network_address + 1)
        print("Last Usable IP:", result.broadcast_address - 1)

except ValueError:
    print("Invalid Input... try entering a correct IP Address")
