#!/user/bin/env python3

import platform
import os

ip = "127.0.0.1"

current_os = platform.system().lower()
if current_os == "windows":
    ping_cmd = f"ping -n 1 -w 2 {ip} > nul"
else:
    ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"

exit_code = os.system(ping_cmd)

print(exit_code)