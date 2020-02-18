from bs4 import BeautifulSoup
import requests

def getLinks(main,s):
    try:
        page = requests.get(main+s)
        soup = BeautifulSoup(page.content,'html.parser')
        links = []
        for i in soup.findAll('a',href=True):
            if('https' in i['href']):
                links.append(i['href'])
            else:
                links.append(main+i['href'])
        return links
    except:
        return None
#print(getLinks("https://en.wikipedia.org","/wiki/Main_Page"))


def BFS(main,source,limit=100):
    queue = [source]
    visited=[main+source]
    while(len(queue)!=0 and len(visited)<limit):
        x = queue[0]
        del queue[0]
        #print(main,x)
        children = getLinks(main,x)
        # print(children)
        if(children!=None):
            for i in children:
                if('https' in i):
                    if(i not in visited):
                        queue.append(i)
                        visited.append(i)
                else:
                    if(main+i not in visited):
                        queue.append(i)
                        visited.append(main+i)
    return visited
y=BFS("https://www.xvideos.com/","",100)
print(y)
print(len(y))
fil = open("links.txt","a")
for i in y:
    fil.write(i+'\n')
