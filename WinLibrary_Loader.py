import ctypes, ctypes.util
import sys, platform

if platform.system() == "Windows":
    path_libc = ctypes.util.find_library("msvcrt")
else:
    path_libc = ctypes.util.find_library("c")

try:
    libc = ctypes.CDLL(path_libc)
except OSError:
    print("Unable to load the C library")
    sys.exit()
print(f'Success in loading the C library from "{path_libc}"')