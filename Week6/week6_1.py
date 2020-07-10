import requests
from bs4 import BeautifulSoup

raw = requests.get("https://v4.map.naver.com",headers={"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text,'html.parser')

# 컨테이너 dl.lsnx_det
stores = html.select("dl.lsnx_det")
print(stores)