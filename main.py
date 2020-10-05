from telegram.ext import Updater, CommandHandler
from telegram import ParseMode
import logging
import random
<<<<<<< HEAD
import animes
=======
from env import TOKEN
>>>>>>> 3d72b80e53cc0084c76bd0d7d940bb28cec9de50
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

def frogsay(update, context):
    fullSpeach = ' '.join(context.args)

    if not fullSpeach:
        fullSpeach = "mai falar oq?"

    while len(fullSpeach) % 17 != 0:
        fullSpeach += " "

    speach = [fullSpeach[i:i+17] for i in range(0, len(fullSpeach), 17)]
    frogAscii = [f"<code>+{17*'-'}+",f"+{17*'-'}+","    \ ","     \ ","       (o)----(o)","       /.______.\ ","       \________/","     ./          \.","     ( .        , )","      \ \_\\\//_/ /   </code>"]

    for i,line in enumerate(speach):
        frogAscii.insert(i+1, f"|{line}|")

    context.bot.send_message(chat_id=update.effective_chat.id, text='\n'.join(frogAscii), parse_mode='html')

sent_images = set()
def dio(update, context):
    image = "./Dio/"
    
    while True:
        pic = random.choice(list(dio_pics.keys()))
        if not sent_images.difference(dio_pics.keys()):
            sent_images.clear()
        if pic not in sent_images:
            sent_images.add(pic)
            break

    image += dio_pics[pic]["img"]
    caption = "<i>" + dio_pics[pic]["cap"] + "</i>"
    
    context.bot.sendPhoto(chat_id=update.message.chat_id, photo=open(image, "rb"), caption=caption, parse_mode="html")

def animealeatorio(update, context):
    chatId = update.message.chat_id
    messageId = update.message.message_id

    infos = animes.randAnime()
    animeData = infos[1]
    id = list(animeData.keys())
    animeInfos = list(animeData[id[5]][0].keys())
    while True:
        animeId = random.randint(1, 305)
        try:
            link = animeData[id[5]][animeId][animeInfos[1]]
            name = animeData[id[5]][animeId][animeInfos[2]]
            break
        except:
            pass
    
    msg = f"Toma aqui otakinho ヽ(*⌒▽⌒*)ﾉ o anime <b>{name}</b> é do ano <b>{infos[0]}</b>:\n{link}"
    context.bot.sendMessage(parse_mode='HTML', chat_id = chatId, text = msg, reply_to_message_id = messageId)


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
<<<<<<< HEAD
    dp.add_handler(CommandHandler("animealeatorio", animealeatorio))
=======
    dp.add_handler(CommandHandler("frogsay", frogsay))
>>>>>>> 3d72b80e53cc0084c76bd0d7d940bb28cec9de50

    updater.start_polling()
    logging.info("=== It's alive! ===")
    updater.idle()
    logging.info("=== Oh no, It's dying! ===")

if __name__ == "__main__":
    main()
