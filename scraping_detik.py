import requests
from bs4 import BeautifulSoup 

r = requests.get('https://www.detik.com')

soup = BeautifulSoup(r.content, 'html.parser')

main = soup.find('div', class_='list-content')

main2 = main.find_all('a', class_='media__link')

five_top = []

for i in range(len(main2)):
    if ((i % 2) == 0):
        five_top.append({'src':main2[i]['href'],'title':main2[i]['dtr-ttl']})

print(five_top)