import wmi

c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]


print(f"SystemFamily: {my_system.SystemFamily}")
print(f"SystemFamily: {my_system.SystemType}")
print(f"SystemFamily: {my_system.NumberOfProcessors}")
print(f"SystemFamily: {my_system.Name}")
print(f"SystemFamily: {my_system.Model}")
print(f"SystemFamily: {my_system.Manufacturer}")

# CREDITS: instagram.com/python.hub