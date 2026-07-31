import win32evtlog
from tabulate import tabulate
from colorama import Fore


def get_security_logs():
    print(Fore.CYAN + "\n========== Windows System Logs ==========\n")

    server = 'localhost'
    logtype = 'System'

    try:
        hand = win32evtlog.OpenEventLog(server, logtype)

        flags = (
            win32evtlog.EVENTLOG_BACKWARDS_READ
            | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        )

        events = win32evtlog.ReadEventLog(hand, flags, 0)

        logs = []

        while events and len(logs) < 20:
            for event in events:
                logs.append([
                    event.TimeGenerated.strftime("%Y-%m-%d %H:%M:%S"),
                    event.EventID & 0xFFFF,
                    event.SourceName
                ])

                if len(logs) >= 20:
                    break

            if len(logs) >= 20:
                break

            events = win32evtlog.ReadEventLog(hand, flags, 0)

        print(tabulate(
            logs,
            headers=["Date & Time", "Event ID", "Source"],
            tablefmt="grid"
        ))

    except Exception as e:
        print(Fore.RED + f"Error: {e}")