import psutil
from colorama import Fore


def get_system_health():
    print(Fore.CYAN + "\n========== System Health ==========\n")

    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    print(f"CPU Usage       : {cpu}%")
    print(f"RAM Usage       : {ram.percent}%")
    print(f"Disk Usage      : {disk.percent}%")
    print(f"Available RAM   : {round(ram.available/(1024**3),2)} GB")