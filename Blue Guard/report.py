import socket
import psutil
import subprocess
import os
from datetime import datetime


def generate_report():
    os.makedirs("reports", exist_ok=True)

    report_path = "reports/audit_report.txt"

    hostname = socket.gethostname()

    try:
        ip = socket.gethostbyname(hostname)
    except:
        ip = "Unavailable"

    process_count = len(psutil.pids())

    try:
        firewall = subprocess.run(
            ["netsh", "advfirewall", "show", "allprofiles"],
            capture_output=True,
            text=True
        ).stdout

        firewall_status = "Enabled" if "State ON" in firewall else "Disabled"

    except:
        firewall_status = "Unknown"

    listening_ports = 0

    try:
        for conn in psutil.net_connections(kind="inet"):
            if conn.status == "LISTEN":
                listening_ports += 1
    except:
        listening_ports = 0

    with open(report_path, "w") as file:

        file.write("=" * 55 + "\n")
        file.write("         BLUEGUARD SECURITY AUDIT REPORT\n")
        file.write("=" * 55 + "\n\n")

        file.write(f"Scan Date : {datetime.now()}\n\n")

        file.write("SYSTEM INFORMATION\n")
        file.write("-----------------------------\n")
        file.write(f"Hostname : {hostname}\n")
        file.write(f"IP Address : {ip}\n\n")

        file.write("FIREWALL STATUS\n")
        file.write("-----------------------------\n")
        file.write(f"{firewall_status}\n\n")

        file.write("RUNNING PROCESSES\n")
        file.write("-----------------------------\n")
        file.write(f"Total Processes : {process_count}\n\n")

        file.write("NETWORK\n")
        file.write("-----------------------------\n")
        file.write(f"Listening Ports : {listening_ports}\n\n")

        file.write("=" * 55 + "\n")
        file.write("Audit Completed Successfully\n")
        file.write("=" * 55 + "\n")

    print(f"\nReport saved successfully!")
    print(f"Location: {report_path}")