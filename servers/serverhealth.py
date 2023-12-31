import psutil
import os
import platform
import time
import socket
from subprocess import call
from prettytable import PrettyTable

# Run an infinite loop to check server health
while True:
    # Clear the screen using a bash command
    call('clear')

    print("========================= Server Health\
          =============================")
        
    # PrettyTable is used to print data in the terminal.
    # t = PrettyTable(<list of headings>)
    # t.add_rol(<list of cell in row>)

    # Server OS Info
    print("\n")
    print("-----Operating System Info----")
    print("\nOperating System Type:", os.name)
    print("\nOperating System:", platform.system())
    print("\nOperating System Version:", platform.release())
    print("\nOperating Bit Architecture:", platform.architecture())
    print("\nComputer Name:", platform.node())
    hostname = platform.node()
    IPAddr = socket.gethostbyname(hostname)
    print("\nComputer IP Address:", IPAddr)
    print("\n")

    # Fetch the Network information
    print("-------Network Status-----")
    table = PrettyTable(['Network', 'Status', 'Speed'])
    for key in psutil.net_if_stats().keys():
        name = key
        up = "Up" if psutil.net_if_stats()[key].isup else "Down"
        speed = psutil.net_if_stats()[key].speed
        table.add_row([name, up, speed])
    print(table)

    # Fetch the memory information
    print("-----Memory Usage-----")
    memory_table = PrettyTable(["Total(GB)", "Used(GB)", 
                                "Available(GB)", "Percentage"])
    vm = psutil.virtual_memory()
    memory_table.add_row([
        f'{vm.total / 1e9:.3f}',
        f'{vm.used / 1e9:.3f}',
        f'{vm.available / 1e9:.3f}',
        vm.percent
    ])
    print(memory_table)
    print("\n")

    # Fetch the disk information
    print("-----Disk Usage-----")
    disk_table = PrettyTable(["Table Usage(GB)", "Used(GB)",
                              "Free(GB)", "Percentage"])
    disk = psutil.disk_usage('/')
    disk_table.add_row([
        f'{disk.total / 1e9:.3f}',
        f'{disk.used / 1e9:.3f}',
        f'{disk.free / 1e9:.3f}',
        disk.percent
    ])

    print(disk_table)
    print("\n")

    # Fetch the 10 processes from available processes that has the highest cpu usage
    print("----Top 10 Processes with Highest CPU Usage----")
    process_table = PrettyTable(["PID", "PNAME","STATUS",
                                 "CPU", "NUM THREADS","MEMORY(GB)"])
    
    proc = []
    # Get the pids from last which mostly are user processes
    for pid in psutil.pids()[-200:]:
        try:
            p = psutil.Process(pid)
            # Trigger cpu percent() the first time which leads to return of 0.0
            p.cpu_percent()
            proc.append(p)

        except Exception as e:
            pass 

    # Sort by cpu percent
    top = {}
    time.sleep(0.1)
    for p in proc:
        # Trigger cpu_percent() the second time for measurement
        top[p] = p.cpu_percent() / psutil.cpu_count()

    top_list = sorted(top.items(), key=lambda x: x[1])
    top10 = top_list[-10:]
    top10.reverse()

    for p, cpu_percent in top10:
        # While fetching the processes, some of the subprocesses may exit
        # Hence we need to put his codein a try-except block.
        try:
            # Oneshot to improve info retrieve efficiency
            with p.oneshot():
                process_table.add_row([
                    str(p.pid),
                    p.name(),
                    p.status(),
                    f'{cpu_percent:.2f}' + "%",
                    p.num_threads(),
                    f'{p.memory_info().rss / 1e6:.3f}'
                ])
        
        except Exception as e:
                pass
        print(process_table)

        # Create a 1 second delay
        time.sleep(1)