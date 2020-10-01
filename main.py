from telegram.ext import Updater, CommandHandler
import logging
import random
from froggies import froggy_pics

def start(update, context):
    s = "Olá, @{}! (• ε •)".format(update.effective_user.username)
    context.bot.send_message(chat_id=update.effective_chat.id, text=s)

def quarentena(update, context):
	context.bot.sendPhoto(chat_id=update.effective_chat.id, photo="https://66.media.tumblr.com/319e7285e04bac7c890d8eb542f26fcd/94b95567e3eef4be-03/s1280x1920/c91e807f40c1860f87855d0d953830b07e0a19db.jpg")

def fofura(update, context):
    g = random.randint(1,100)
    gg = (100-g)
    f = "O nível de fofura de @{} é {}% e o seu nível de arch user é {}%! (´｡• ᵕ •｡`)".format(update.effective_user.username, g, gg)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f)

def distro(update, context):
    lista = ['Debian','Arch','Fedora','Ubuntu','Linux Mint','Manjaro','Gentoo','CentOS','Kali','elementary OS','Puppy','Parrot','Peppermint OS','Oracle']
    h = "Parabéns, @{}! Sua distro é {}! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧'".format(update.effective_user.username, random.choice(lista))
    context.bot.send_message(chat_id=update.effective_chat.id, text=h)

def hal(update, context):
    abc = "I'm sorry, @{}. I'm afraid I can't do that.".format(update.effective_user.username)
    context.bot.send_message(chat_id=update.effective_chat.id, text=abc)

def corona(update, context):
	context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('corona.mp3', 'rb'))

def froggypic(update, context):
    randomPhoto = random.choice(list(froggy_pics.keys()))
    image = froggy_pics[randomPhoto]["img"]
    caption = froggy_pics[randomPhoto]["cap"]
    context.bot.sendPhoto(chat_id=update.message.chat_id, photo=open(image, "rb"), caption=caption, parse_mode="html")

def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")

    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("quarentena", quarentena))
    dp.add_handler(CommandHandler("fofura", fofura))
    dp.add_handler(CommandHandler("distro", distro))
    dp.add_handler(CommandHandler("hal", hal))
    dp.add_handler(CommandHandler("corona", corona))
    dp.add_handler(CommandHandler("froggypic", froggypic))

    updater.start_polling()
    logging.info("=== It's alive! ===")
    updater.idle()
    logging.info("=== Oh no, It's dying! ===")


if __name__ == "__main__":
    main()
