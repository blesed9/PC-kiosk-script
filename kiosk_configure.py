import subprocess
import os
import time

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try " \
    "again, this time using 'sudo'. Exiting.")
else: pass
time.sleep(2)


def update_system():
    print("Update system...")
time.sleep(2)
os.system("apt-get update")
os.system("apt-get upgrade -y")
os.system("sudo apt install xorg openbox chromium-browser unclutter lightdm -y")

time.sleep(2)




