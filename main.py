import ipaddress

def calc_network_address(ip_addr, netmask):
    ip = int(ipaddress.IPv4Address(ip_addr))
    mask = int(ipaddress.IPv4Address(netmask))

    network = ip & mask

    return str(ipaddress.IPv4Address(network))


if __name__ == "__main__":
    ip = "192.168.1.10"
    mask = "255.255.255.0"

    result = calc_network_address(ip, mask)

    print(result)
