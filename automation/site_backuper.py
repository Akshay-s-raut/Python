import requests, re , urllib.request
from bs4 import BeautifulSoup

link = input()
res = requests.get(link)
res.raise_for_status()

resp = urllib.request.urlopen(link)
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

#do a BFS
visited = []
def BFS(node):
    if len(visited)==1000:
        return
    linkElems=[]
    try:
        for link in soup.find_all('a', href=True):
            linkElems.append(link['href'])
    except:
        return
    for i in linkElems:
        if i not in visited:
            visited.append(link + i)
            BFS(i)
BFS(link)
print(visited)
