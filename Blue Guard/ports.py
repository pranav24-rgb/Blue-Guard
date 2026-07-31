import psutil
from tabulate import tabulate
from colorama import Fore


def get_open_ports():
    print(Fore.CYAN + "\n========== Open Ports ==========\n")

    ports = []

    try:
        connections = psutil.net_connections(kind='inet')

        for conn in connections:
            if conn.status == "LISTEN":
                protocol = "TCP"

                if conn.type == 2:
                    protocol = "UDP"

                ip = conn.laddr.ip
                port = conn.laddr.port
                pid = conn.pid

                ports.append([protocol, ip, port, conn.status, pid])

        ports.sort(key=lambda x: x[2])

        print(tabulate(
            ports,
            headers=["Protocol", "Local Address", "Port", "Status", "PID"],
            tablefmt="grid"
        ))

        print(Fore.GREEN + f"\nTotal Listening Ports: {len(ports)}")

    except Exception as e:
        print(Fore.RED + f"Error: {e}")