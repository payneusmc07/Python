import ctypes

user_handle = ctypes.WinDLL("User32.dll")  # Handle for user32.dll

hWnd = None  # None is inplace of NULL
lpText = "OWNED!!!"
lpCaption = "Message Box"
uType = 0x00000001  # OK, Cancel message box

response = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType) # parameters must be passed in order

# Error handling,
k_handle = ctypes.WinDLL("Kernel32.dll") # Kernel32.dll
error = k_handle.GetLastError()

if error != 0:
    print("Error Code: {0}".format(error))
    exit(1)
if response == 1:
    print("The User Clicked OK")
elif response == 2:
    print("The User Clicked Cancel")

