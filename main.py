import ipaddress


def calc_network_address(ip_addr, netmask):
    ip = int(ipaddress.IPv4Address(ip_addr))
    mask = int(ipaddress.IPv4Address(netmask))

    network = ip & mask

    return str(ipaddress.IPv4Address(network))


if __name__ == "__main__":
    ip = input("IPアドレスを入力してください: ")
    netmask = input("ネットマスクを入力してください: ")

    result = calc_network_address(ip, netmask)

    print("ネットワークアドレス:", result)
