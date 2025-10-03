import subprocess
import os
import time

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try " \
    "again, this time using 'sudo'. Exiting.")
else: pass
time.sleep(2)
url = input("Podaj adres strony dla kiosku (np. https://example.com): ").strip()

def update_system():
    print("Update system...")
time.sleep(2)
os.system("apt-get update")
os.system("apt-get upgrade -y")

time.sleep(2)
def package_installation():
    print("Installation of packages...")
    time.sleep(2)
os.system("sudo apt install xorg openbox chromium-browser lightdm ufw -y")

time.sleep(2)
def start_lightDM():
    print("Starting LightDM...")
os.system("systemctl enable lightdm -y")
os.system("systemctl set-default graphical.target")

time.sleep(2)
def create_user():
    print("Creating a user")
os.system("adduser kiosk")
os.system("usermod -aG audio,video kios")

time.sleep()
def create_files():
    print("Creating a files")
os.system("nano /etc/lightdm/lightdm.conf")


os.system("-u kiosk mkdir -p /home/kiosk/.config/openbox")
os.system("-u kiosk nano /home/kiosk/.config/openbox/autostart")
os.system('echo -e "[Seat:*]\\nautologin-user=kiosk\\nautologin-user-timeout=0" | sudo tee -a /etc/lightdm/lightdm.conf')

time.sleep(2)





