from telegram.ext import Updater, CommandHandler
import logging
import random
from froggies import froggy_pics
from dio import dio_pics

def start(update, context):
    s = "Olá, @{}! (• ε •)".format(update.effective_user.username)
    context.bot.send_message(chat_id=update.effective_chat.id, text=s)

def quarentena(update, context):
    imgURL = "https://66.media.tumblr.com/319e7285e04bac7c890d8eb542f26fcd/94b95567e3eef4be-03/s1280x1920/c91e807f40c1860f87855d0d953830b07e0a19db.jpg"
    context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=imgURL)

def fofura(update, context):
    cuteLevel = random.randint(1, 100)
    archLevel = 100 - cuteLevel

    s = "O nível de fofura de @{} é {}% e o seu nível de arch user é {}%! (´｡• ᵕ •｡`)".format(update.effective_user.username, cuteLevel, archLevel)
    context.bot.send_message(chat_id=update.effective_chat.id, text=s)

def distro(update, context):
    distros = ["Debian",
               "Arch",
               "Fedora",
               "Ubuntu",
               "Linux Mint",
               "Manjaro",
               "Gentoo",
               "CentOS",
               "Kali",
               "Elementary OS",
               "Puppy",
               "Parrot",
               "Peppermint OS",
               "Oracle"]

    s = "Parabéns, @{}! Sua distro é {}! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧'".format(update.effective_user.username, random.choice(distros))
    context.bot.send_message(chat_id=update.effective_chat.id, text=s)

def hal(update, context):
    s = "I'm sorry, @{}. I'm afraid I can't do that.".format(update.effective_user.username)
    context.bot.send_message(chat_id=update.effective_chat.id, text=s)

def corona(update, context):
    context.bot.send_audio(chat_id=update.effective_chat.id, audio=open("corona.mp3", "rb"))

def froggypic(update, context):
    randomPhoto = random.choice(list(froggy_pics.keys()))
    image = froggy_pics[randomPhoto]["file"]
    caption = "<i>" + froggy_pics[randomPhoto]["caption"] + "</i>"
    context.bot.sendPhoto(chat_id=update.message.chat_id, photo=open(image, "rb"), caption=caption, parse_mode="html")

def asterisco(update, context):
    """
    oi kibon -> ** *****
    oi #kibon# -> oi *****
    oi #kibon# tudo #bem# -> oi ***** tudo ***
    """

    message = " ".join(context.args)
    if not message: return

    s = ""
    if "#" not in message:
        s = " ".join("*"*len(word) for word in message)
    elif message.count("#") % 2 == 0:
        makeStar = False
        for c in message:
            if c == "#":
                makeStar = not makeStar
            else:
                s += ("*" if makeStar else c)
    else:
        s = "@{}, você não formatou sua entrada corretamente".format(update.effective_user.username)

    context.bot.send_message(chat_id=update.effective_chat.id, text=s)

def dio(update, context):
    image = "./Dio/"
    index = random.choice(list(dio_pics.keys()))
    image += dio_pics[index]["img"]
    caption = "<i>" + dio_pics[index]["cap"] + "</i>"
    context.bot.sendPhoto(chat_id=update.message.chat_id, photo=open(image, "rb"), caption=caption, parse_mode="html")

def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")

    updater = Updater(token="1377675743:AAGOPVoJK8GcRnLR6OW8uueIpud4aPNSyao", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("quarentena", quarentena))
    dp.add_handler(CommandHandler("fofura", fofura))
    dp.add_handler(CommandHandler("distro", distro))
    dp.add_handler(CommandHandler("hal", hal))
    dp.add_handler(CommandHandler("corona", corona))
    dp.add_handler(CommandHandler("froggypic", froggypic))
    dp.add_handler(CommandHandler("asterisco", asterisco))
    dp.add_handler(CommandHandler("dio", dio))

    updater.start_polling()
    logging.info("=== It's alive! ===")
    updater.idle()
    logging.info("=== Oh no, It's dying! ===")

if __name__ == "__main__":
    main()
