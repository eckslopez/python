import wmi

try:
    # print("Establishing connectio to %s", %ip)
    connection = wmi.WMI()

    for os in connection.Win32_OperatingSystem():
        print("OS Edition: ", os.caption)
        print("Free: ", os.FreePhysicalMemory)
        print("Total: ", os.TotalVisibleMemorySize)
        print("Build Number: ", os.BuildNumber)
        print(os.BuildType)

        print(os.Name)
        print(os.Organization)
        print(os.OSArchitecture)

    for system in connection.Win32_ComputerSystem():
        print(system.name)
        print(system.NumberOfLogicalProcessors)
        print(system.NumberOfProcessors)
        print(system.status)
        print(system.SystemType)

    print()
    print("Network")

    print()
    for network in connection.Win32_NetworkAdapterConfiguration():
        print(network.Caption)
        print(network.MACAddress)
        if (network.IPAdress != None):
            for (address, subnet) in zip(network.IPAddress, network.IPSubnet):
                print("Assigned Address: {}, Mask: {}".format(address, subnet))

except Exception as e:
    print(e)