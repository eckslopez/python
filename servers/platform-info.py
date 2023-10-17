import platform

# https://docs.python.org/3/library/platform.html
my_system = platform.uname() # Only contains the six below that can also be called individually

print(f"Node Name: {my_system.node}")
print(f"System: {my_system.system}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")

# Separate from uname
print(f"Platform: {platform.platform()}")
print(f"Architecture: {platform.architecture()}")
print(f"Python Version: {platform.python_version_tuple()}")
print(f"Python Implementation: {platform.python_implementation()}")

# Windows Specific
print(f"Windows (WIN32) Version: {platform.win32_ver()}") 
print(f"Windows (WIN32) Edition: {platform.win32_edition()}")
print(f"Windows (WIN32) IoT: {platform.win32_is_iot()}") # Formerly Windows Embedded