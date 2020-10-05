import jikanpy
import random
import json
import time

jikan = jikanpy.Jikan()

def randAnime():
    animeYear = random.randint(1995, 2020) #Years that we'll search for the animes
    season = ["Fall", "Winter", "Spring", "Summer"] #Season that we'll search for the animes
    
    random.shuffle(season) #Chosing a random season

    #Trying to get a json from the myanimelist based on the random season and year
    while True:
        try:
            animeData = jikan.season(year = animeYear, season = season[0])
            break
        except:
            time.sleep(4)
            pass
    
    #Creating a list that will 
    infos = [animeYear, animeData]

    #Returning the list to the main containing the json of the anime an the random year choosen
    return infos