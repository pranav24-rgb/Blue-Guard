from colorama import Fore, init

# Import project modules
from network import get_network_info
from firewall import get_firewall_status
from processes import get_running_processes
from ports import get_open_ports
from logs import get_security_logs
from report import generate_report
from system_health import get_system_health
from dashboard import show_dashboard

# Initialize Colorama
init(autoreset=True)


def display_banner():
    print(Fore.CYAN + "=" * 70)
    print(Fore.CYAN + "              BLUEGUARD SECURITY AUDIT TOOL")
    print(Fore.CYAN + "=" * 70)


def display_menu():
    print(Fore.YELLOW + "\nSelect an option:\n")
    print("1. Network Information")
    print("2. Firewall Status")
    print("3. Running Processes")
    print("4. Open Ports")
    print("5. Windows System Logs")
    print("6. Generate Security Report")
    print("7. System Health")
    print("8. Security Dashboard")
    print("9. Exit")
    print(Fore.CYAN + "=" * 70)


def menu():
    while True:
        display_banner()
        display_menu()

        choice = input(Fore.GREEN + "\nEnter your choice (1-9): ")

        if choice == "1":
            print(Fore.GREEN + "\nLoading Network Information...\n")
            get_network_info()

        elif choice == "2":
            print(Fore.GREEN + "\nChecking Firewall Status...\n")
            get_firewall_status()

        elif choice == "3":
            print(Fore.GREEN + "\nFetching Running Processes...\n")
            get_running_processes()

        elif choice == "4":
            print(Fore.GREEN + "\nScanning Open Ports...\n")
            get_open_ports()

        elif choice == "5":
            print(Fore.GREEN + "\nReading Windows System Logs...\n")
            get_security_logs()

        elif choice == "6":
            print(Fore.GREEN + "\nGenerating Security Report...\n")
            generate_report()

        elif choice == "7":
            print(Fore.GREEN + "\nChecking System Health...\n")
            get_system_health()

        elif choice == "8":
            print(Fore.GREEN + "\nOpening Security Dashboard...\n")
            show_dashboard()

        elif choice == "9":
            print(Fore.CYAN + "\n" + "=" * 70)
            print("        Thank you for using BlueGuard!")
            print("      Windows Security Audit Completed")
            print("           Stay Safe • Stay Secure")
            print("=" * 70)
            break

        else:
            print(Fore.RED + "\n❌ Invalid choice! Please enter a number between 1 and 9.")

        input(Fore.MAGENTA + "\nPress Enter to return to the Main Menu...")


if __name__ == "__main__":
    menu()