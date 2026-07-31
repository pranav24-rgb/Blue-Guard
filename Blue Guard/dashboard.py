import socket
import platform
import subprocess
import psutil
from colorama import Fore


def get_firewall_status():
    """
    Returns True if ALL firewall profiles are ON.
    """

    try:
        result = subprocess.run(
            ["netsh", "advfirewall", "show", "allprofiles"],
            capture_output=True,
            text=True
        )

        output = result.stdout.upper()

        on_count = output.count("STATE                                 ON")

        return on_count >= 3

    except:
        return False


def get_color(value):
    """
    Returns color based on usage percentage.
    """

    if value < 60:
        return Fore.GREEN

    elif value < 80:
        return Fore.YELLOW

    else:
        return Fore.RED


def show_dashboard():

    print(Fore.CYAN + "\n" + "=" * 72)
    print(Fore.CYAN + "                 BLUEGUARD SECURITY DASHBOARD")
    print(Fore.CYAN + "=" * 72)

    # --------------------------------------------------

    hostname = socket.gethostname()

    try:
        ip = socket.gethostbyname(hostname)
    except:
        ip = "Unavailable"

    os_name = platform.system() + " " + platform.release()

    # --------------------------------------------------

    cpu = psutil.cpu_percent(interval=1)

    ram = psutil.virtual_memory()

    disk = psutil.disk_usage('/')

    process_count = len(psutil.pids())

    # --------------------------------------------------

    ports = 0

    try:

        for conn in psutil.net_connections(kind="inet"):

            if conn.status == "LISTEN":
                ports += 1

    except:
        pass

    # --------------------------------------------------

    firewall_enabled = get_firewall_status()

    firewall_text = "Enabled" if firewall_enabled else "Disabled"

    firewall_color = Fore.GREEN if firewall_enabled else Fore.RED

    # --------------------------------------------------

    print(f"Computer Name      : {hostname}")
    print(f"Operating System   : {os_name}")
    print(f"Local IP Address   : {ip}")

    print(f"Firewall           : {firewall_color}{firewall_text}{Fore.RESET}")

    print()

    print(get_color(cpu) + f"CPU Usage          : {cpu:.1f}%")

    print(get_color(ram.percent) + f"RAM Usage          : {ram.percent:.1f}%")

    print(get_color(disk.percent) + f"Disk Usage         : {disk.percent:.1f}%")

    print(Fore.CYAN + f"Running Processes  : {process_count}")

    print(Fore.CYAN + f"Listening Ports    : {ports}")

    # --------------------------------------------------

    score = 100

    if not firewall_enabled:
        score -= 35

    if cpu > 85:
        score -= 20

    elif cpu > 70:
        score -= 10

    if ram.percent > 90:
        score -= 20

    elif ram.percent > 75:
        score -= 10

    if disk.percent > 90:
        score -= 10

    if ports > 80:
        score -= 10

    if score < 0:
        score = 0

    print(Fore.CYAN + "\n" + "=" * 72)

    print(Fore.CYAN + f"Security Score     : {score}/100")

    if score >= 80:

        print(Fore.GREEN + "Overall Status     : 🟢 SAFE")

    elif score >= 60:

        print(Fore.YELLOW + "Overall Status     : 🟡 MODERATE")

    else:

        print(Fore.RED + "Overall Status     : 🔴 HIGH RISK")

    print(Fore.CYAN + "=" * 72)