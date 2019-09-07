#
#    VK Auto Status
#   [ Stolar Studio ]
#

ver = "0.1.0"

import vk_api, requests
import datetime, time
import configparser, os

if not os.path.exists("settings.txt"):
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "login", "")
    config.set("Settings", "password", "")
    with open("settings.txt", "w") as config_file:
        config.write(config_file)
    print("write login and password in settings.txt")
    exit()

config = configparser.ConfigParser()
config.read("settings.txt")
login = config.get("Settings", "login")
password = config.get("Settings", "password")

session = requests.Session()
vk = vk_api.VkApi(login, password)

vk.auth(token_only=True)

print("\n [ Stolar Studio ]\n  VK Auto Status\n")

while True:
    #vk =

    delta = datetime.timedelta(hours=3, minutes=0)
    t = (datetime.datetime.now(datetime.timezone.utc)+delta)

    nowtime = t.strftime("%H:%M")
    nowdate = t.strftime("%d.%m.%Y")

    on = vk.method("friends.getOnline")
    counted = len(on)

    vk.method("status.set", {"text": nowtime + " | " + nowdate + " | " + "Друзей онлайн: " + str(counted)})

    time.sleep(30)
