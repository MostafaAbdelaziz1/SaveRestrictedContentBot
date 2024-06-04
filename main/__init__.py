#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("26668313", default=None, cast=int)
API_HASH = config("eda1555ec1e1b280ab1864a82ec7ff7a", default=None)
BOT_TOKEN = config("7444885436:AAG4x1Cw7HZI4AT8gRqL1JPePMVwe9QPXZ4", default=None)
SESSION = config("BAGW7RkAIen8AK3zBz7UimnRogn0_s-cJzmDPFuGDhjfU0i6ptSA_OOEVsW9ZQdspNqBc21f7VkUi59XiDMIg6bI6bEHae_HwBsQGT9rH8F5RovPHGgunK4N_0hmAXprpjGBWnDkvueYKGm1cCivElICo-Ph_aKej9XENLh5M8g92hZ3fg1ZpQfe8PRkgkWS3Gz1bcY7nNGTSxrKhFLOID9D2JYMaSAgGnFwps9QK2Mb-vXhTF77aTlPENUDnkm2_w_Dw7PM8IBpuFhApezjl76h7utstY3cZsdwXvuKeD9qVa5rwpscb6MscU7JSR291uSTQ80mnursKSywI6soVc9I2yjv4QAAAAG7v8AQ", default=None)
FORCESUB = config("mxkddhsbssgsyshwjalalajssbebwhs", default=None)
AUTH = config("845948197", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
