import psutil, sys

# Overall CPU utilization, based on interval
'''
try:
    while True:
        print(psutil.cpu_percent(interval=3, percpu=True))
except KeyboardInterrupt:
    print("Stopping")
    sys.exit(0)
except Exception as e:
    print(e)
'''

# CPU percent per process, based on interval
'''
p = psutil.Process(4320) # Number represents PID
try:
    while True:
        print("The process {} has a rolling utilization of {}%".format(p.name(),p.cpu_percent(interval=3)))
except KeyboardInterrupt:
    print("Stopping")
    sys.exit(0)
except Exception as e:
    print(e)
'''
'''
# System memory usage
vm = psutil.virtual_memory()
print("Total memory: {} bytes".format(("{:,}".format(vm.total)))) 
print("Used memory: {} bytes".format(("{:,}".format(vm.used)))) 
print("Used memory percentage: {}%".format(("{:,}".format(vm.percent)))) 
print("Available memory: {} bytes".format(("{:,}".format(vm.free)))) 
'''

# Checking memory use of speific process
'''
p = psutil.Process(8632)
pm = p.memory_info().rss # RSS = this is the non-swapped physical memory a process has used
print("The {} process is using {} bytes of physical memory".format(p.name(), ("{:,}".format(pm))))
'''