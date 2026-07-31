import psutil
from tabulate import tabulate
from colorama import Fore


def get_running_processes():
    print(Fore.CYAN + "\n========== Running Processes ==========\n")

    process_list = []

    for process in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            pid = process.info['pid']
            name = process.info['name']

            memory = round(process.info['memory_info'].rss / (1024 * 1024), 2)

            cpu = process.cpu_percent(interval=0.1)

            process_list.append([pid, name, cpu, memory])

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    process_list = sorted(process_list, key=lambda x: x[3], reverse=True)

    print(tabulate(
        process_list[:20],
        headers=["PID", "Process Name", "CPU %", "Memory (MB)"],
        tablefmt="grid"
    ))