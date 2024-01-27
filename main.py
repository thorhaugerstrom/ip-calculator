def ip_to_binary(ip_address):
    octets = ip_address.split('.')

    binary_octets = [format(int(octet), '08b') for octet in octets]

    binary_ip = '.'.join(binary_octets)

    return binary_ip


if __name__ == "__main__":
    ip_address = input("Enter the IP address to be converted: ")
    binary_ip = ip_to_binary(ip_address)

    print(f"Binary IP Address: {binary_ip}")