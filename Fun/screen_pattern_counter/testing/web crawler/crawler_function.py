from bs4 import BeautifulSoup
import requests

def getLinks(main,s):
    page = requests.get(main+s)
    #print(soup.prettify())
    if(page.status_code !=200):
        return None
    else:
        soup = BeautifulSoup(page.content,'html.parser')
        links = []
        for i in soup.findAll('a',href=True):
            if('https' in i['href']):
                links.append(i['href'])
            else:
                links.append(main+i['href'])
        return links

y=getLinks("https://www.youtube.com/","")
for i in y:
    print(i)


# page = requests.get("nolink")
# soup = BeautifulSoup(page.content,'html.parser')
# print(soup.prettify())
