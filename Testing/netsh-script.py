'''
Python Script to show all available wlan-networks
using the subprocess module and the netsh command

'''

import subprocess

# netsh command for showing all available wlan-networks
command = ["netsh", "wlan", "show", "networks", "mode=bssid"]


output = subprocess.run(command, capture_output=True)

# print captured standard-output and decode; NOTE: errors must be ignored, else unicode error occurs
print(output.stdout.decode(errors="ignore"))