from pyrogram import Client
import json
import time
import random


class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'


config = open(r"config.json", "r")
config = json.loads(config.read())

app = Client(
    session_name="0x1D",
    api_id=config["api_id"],
    api_hash=config["api_hash"]
    )


def kullaniciCek(app):
    count = 0
    for channel in app.get_dialogs():
        if "group" in channel.chat.type:
            print(f"""{bcolors.OKBLUE}[ {bcolors.OKGREEN}{count}{bcolors.OKBLUE} ] - """ + str(channel.chat.title))
        count += 1

    g_index = int(input("chat seç: "))
    chatId = app.get_dialogs()[g_index].chat.id
    g_index = int(input("üye eklenecek chat seç: "))
    chatIdEklenecek = app.get_dialogs()[g_index].chat.id

    counter = 0
    chhh = app.get_chat_members(chatId)
    for i in chhh:
        try:
            rndm = random.randrange(len(chhh)-1)

            app.add_chat_members(chatIdEklenecek, chhh[rndm].user.id)
            counter += 1
            print(i.user.first_name + " eklendi - Toplam eklenen sayısı: " + counter)
        except:
            print("eklenemedi")
        time.sleep(8)


with app:
    kullaniciCek(app)

app.run()
