import subprocess
from colorama import Fore


def get_firewall_status():
    print("\n========== Windows Firewall Status ==========\n")

    try:
        result = subprocess.run(
            ["netsh", "advfirewall", "show", "allprofiles"],
            capture_output=True,
            text=True
        )

        output = result.stdout

        for line in output.splitlines():
            if "Domain Profile Settings" in line:
                print(Fore.CYAN + "\nDomain Firewall")

            elif "Private Profile Settings" in line:
                print(Fore.CYAN + "\nPrivate Firewall")

            elif "Public Profile Settings" in line:
                print(Fore.CYAN + "\nPublic Firewall")

            elif "State" in line:
                if "ON" in line:
                    print(Fore.GREEN + line.strip())
                elif "OFF" in line:
                    print(Fore.RED + line.strip())

    except Exception as e:
        print(Fore.RED + f"Error: {e}")