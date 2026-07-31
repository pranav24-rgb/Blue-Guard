import socket
import psutil


def get_network_info():
    print("\n========== Network Information ==========")

    # Hostname
    hostname = socket.gethostname()
    print(f"Hostname      : {hostname}")

    # Local IP Address
    try:
        ip = socket.gethostbyname(hostname)
    except:
        ip = "Unable to get IP"

    print(f"Local IP      : {ip}")

    # MAC Address
    mac = psutil.net_if_addrs()

    print("\nNetwork Interfaces:")

    for interface, addresses in mac.items():
        print(f"\n{interface}")

        for addr in addresses:
            print(f"   Family : {addr.family}")
            print(f"   Address: {addr.address}")