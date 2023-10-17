import psutil
import pprint
import tabulate

# Complie processes into dictionary
# process_dict = {}
for proc in psutil.process_iter(['pid','ppid','name','username']):
    print(proc.info)