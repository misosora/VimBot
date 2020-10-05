import jikanpy
import random
import json
import time

jikan = jikanpy.Jikan()

def randAnime():
    animeYear = random.randint(1995, 2020)
    season = ["Fall", "Winter", "Spring", "Summer"]
    
    random.shuffle(season)

    while True:
        try:
            animeData = jikan.season(year = animeYear, season = season[0])
            break
        except:
            time.sleep(4)
            pass
    
    infos = [animeYear, animeData]

    return infos