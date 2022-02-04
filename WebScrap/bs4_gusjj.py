import requests
from bs4 import BeautifulSoup
import math


url = 'https://comic.naver.com/webtoon/weekday.nhn'
url = 'https://comic.naver.com/webtoon/list.nhn?titleId=675554'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

cartoons = soup.find_all('div', attrs={"class": "rating_type"})
ratings = []
for cartoon in cartoons:
    ratings.append(float(cartoon.find("strong").get_text()))

print("총 점수 : %f" % (sum(ratings)))
print("평균 점수 : {0:0.2f}".format((sum(ratings)/len(ratings))))
