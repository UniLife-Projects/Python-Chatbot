import re
import requests as req

LINK = "https://en.wikipedia.org/w/api.php"

session = req.Session()

def getWikiConclusion(page_Explored):
    confines = {
        "action": "query",
        "srsearch": page_Explored,
        "format": "json",
        "list": "search",
    }

    get = session.get(url=LINK, params=confines)
    blank = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    outcome = []
    data = get.json()
    
    for entity in data['query']['search']:
        build = entity['snippet']
        blanktext = re.sub(blank, '', build)
        outcome.append(blanktext)
    return outcome
    

