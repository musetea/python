import requests
from bs4 import BeautifulSoup
import re


url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text)

item_class = re.compile("^search-product")
items = soup.find_all("li", attrs={"class": item_class})
print(items[0].find("div", attrs={"class": "name"}).get_text())
