import requests as req

MY_FLICKR = "ff0fa4efb379af58de43bf1c8da3a7cc"

def getPicture(pic):
    link = "https://farm{f}.staticflickr.com/{s}/{i}_{sec}".format(f=pic['farm'], s=pic["server"], sec=pic['secret'])
    link = link + '.jpg'
    return link


def getFlickredAfterMath(mark):
  listed_Links = []

  get = ""
  info = ""

  LINK = "https://api.flickr.com/services/rest"

  confines = {
  'api_key': MY_FLICKR,
  'method': 'flickr.photos.search',
  'text': mark,
  'nojsoncallback': 1, 
  'per_page': 12,
  'sort': 'interestingness-desc',
  'license': '4',
  'format': 'json',
  'extras': 'owner_name,license',
}

  get = req.get(url=LINK,params=confines)
  info = get.json()
  linkImages = map(getPicture,info['photos']['photo'])
  
  for link in linkImages:
    listed_Links.append(link)
  return listed_Links
  
