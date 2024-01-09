# This little project requires proper dependency management.
import wmi_client_wrapper

wmic = wmi_client_wrapper.WmiClientWrapper(hostname="")
for processor in wmic.query("SELECT * FROM Win32_Processor"):
    print(processor["Name"])


'''
ip = ""
username = r""
password = ""
proc=open('C:\\somedir', 'w')

try:
    print("Establishing a connection to %s" %ip)
    connection = wmi.WMI(ip, user=username, password=password)
    #connection = wmi.WMI(ip)
    print("Connection established")

    print()
    print("Operating System:")
    for os in connection.Win32_OperatingSystem():
        print("OS Edition: ", os.caption)
        print("Free Memory: ", os.FreePhysicalMemory)
        print("Total Memory: ", os.TotalVisibleMemorySize)
        print("Build Number: ", os.BuildNumber)
        
        print("Name :", os.Name)
        print("Architecture :", os.OSArchitecture)

    for process in connection.Win32_Process():
        print("ID: {0}\nProcessName: {1}\n".formmat(process.ProcessId,process.Name))
        print(process.Caption)

    print()
    print("Computer System:")
    for system in connection.Win32_CompterSystem():
        print("Name :", system.name)
        print("Logical Processors :", system.NumberOfLogicalProcessors)
        print("Physical Processors (Cores) :", system.NumberOfProcessors)

    print()
    print("Networking:")
    for network in connection.Win32_NetworkAdapterConfiguration():
        print(network.Caption)

        if(network.MACAddress != None):
            print("MAC Address:", network.MACAddress)
        if(network.IPAddress != None):
            for(address,subnet) in zip(network.IPAddress, network.IPSubnet):
                print("Assigned Address: {}, Mask: {}".format(address, subnet))
        print(network.MTU)
        print(network.NumForwardPackets)
        print(network.TcpWindowSize)
        print(network.TcpNumConnections)

except Exception as e:
    print(e)
    #print("Your Username and Password of '+getfqdn(ip)+' are wrong.")

'''