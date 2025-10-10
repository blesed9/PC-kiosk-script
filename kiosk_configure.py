import subprocess
import os
import time

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try " \
    "again, this time using 'sudo'. Exiting.")
else: pass
time.sleep(2)
#url = input("Podaj adres strony dla kiosku (np. https://example.com): ").strip()

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

time.sleep(2)
def create_files():
    print("Creating a files")
os.system("nano /etc/lightdm/lightdm.conf")
time.sleep(2)
os.system("-u kiosk mkdir -p /home/kiosk/.config/openbox")
time.sleep(1)
os.system("-u kiosk nano /home/kiosk/.config/openbox/autostart")
time.sleep(1)
os.system('echo -e "[Seat:*]\\nautologin-user=kiosk\\nautologin-user-timeout=0" | sudo tee -a /etc/lightdm/lightdm.conf')
time.sleep(2)
os.system('echo "#!/bin/bash && xmodmap -e \\"keycode 133 = \\" && xmodmap -e \\"keycode 64 = \\" && xmodmap -e \\"keycode 37 = \\" && xmodmap -e \\"keycode 135 = \\" && xmodmap -e \\"keycode 107 = \\" && xset s off && xset -dpms && xset s noblank && unclutter -idle 3 -root & KIOSK_URL=\\"https://strona-egzaminu.pl\\" && chromium --kiosk \$KIOSK_URL --no-first-run --disable --disable-translate --disable-infobars --disable-suggestions-service --disable-save-password-bubble --disable-session-crashed-bubble --disable-pinch --incognito --password-store=basic & while true; do sleep 15; if ! pgrep chromium > /dev/null; then chromium --kiosk \$KIOSK_URL --no-first-run --disable --disable-translate --disable-infobars --disable-suggestions-service --disable-save-password-bubble --disable-session-crashed-bubble --disable-pinch --incognito --password-store=basic & fi; done" > kiosk.sh')
time.sleep(1)
os.system("chmod +x /home/kiosk/.config/openbox/autostart")
time.sleep(1)
os.system("chown -R kiosk:kiosk /home/kiosk/.config")
time.sleep(1)
os.system("reboot")

