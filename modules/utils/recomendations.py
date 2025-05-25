import random
import requests
import json

def pegar_anime():
    id = random.randint(20, 60000)
    sugestion = requests.get(f"https://api.jikan.moe/v4/anime/{id}")
    r = sugestion.json()
    return r

def mandar(): 
    try:
        r = pegar_anime()
        url = (r.get('data').get('url'))
        title = (r.get('data').get('title'))
        return url, title
    except:
        mandar()

mandar()