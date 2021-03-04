import ctypes

"""
OpenProcess Function:

C++ Syntax
HANDLE OpenProcess(
    DWORD dwDesiredAccess;
    BOOL bInheritHandle;
    DWORD dwProcessId;
);
Parameters must be passed in order displayed in C++ function
Use task manager to find desired PID
Process must be running in order to use it
Error Code 5 is generated is admin rights are needed
"""
# UAC generates a new token for a process that is elevated to admin

k_handle = ctypes.WinDLL("Kernel32.dll")

PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)  # Using logical OR to pipe all access types
dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False
dwProcessId = 0x570  # PID 1392 in hex

# Error handling, error 87, invalid parameter
response = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)
error = k_handle.GetLastError()

if error != 0:
    print("Error Code: {0}".format(error))
    exit(1)
if response <= 0:
    print("Handle was not created")
else:
    print("Handle was created with PID {0}".format(response))
