#
#    VK Auto Status
#   [ Stolar Studio ]
#

ver = "0.1.2"

import vk_api, requests
import datetime, time
import configparser, os

if not os.path.exists("settings.txt"):
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "login", "")
    config.set("Settings", "password", "")
    config.set("Settings", "timer", "59")
    with open("settings.txt", "w") as config_file:
        config.write(config_file)
    print("write login and password in settings.txt")
    exit()

config = configparser.ConfigParser()
config.read("settings.txt")
login = config.get("Settings", "login")
password = config.get("Settings", "password")
timer = config.get("Settings", "timer")

session = requests.Session()
vk = vk_api.VkApi(login, password)

vk.auth(token_only=True)

print("\n [ Stolar Studio ]\n  VK Auto Status\n")

delta = datetime.timedelta(hours=3, minutes=0)
t = (datetime.datetime.now(datetime.timezone.utc)+delta)

print("CHECK TIME...")
oldtime = t.strftime("%M")
while True:
    t = (datetime.datetime.now(datetime.timezone.utc)+delta)
    if not(oldtime == t.strftime("%M")):
        print("TIME OK")
        break
        

while True:
    delta = datetime.timedelta(hours=3, minutes=0)
    t = (datetime.datetime.now(datetime.timezone.utc)+delta)

    nowtime = t.strftime("%H:%M")
    nowdate = t.strftime("%d.%m.%Y")

    on = vk.method("friends.getOnline")
    counted = len(on)
    
    vk.method("status.set", {"text": nowtime + " | " + nowdate + " | " + "Друзей онлайн: " + str(counted)})
    print("STATUS SET ( "+nowtime + " | " + nowdate + " | " + "Друзей онлайн: " + str(counted)+" )")
    time.sleep(int(timer))
