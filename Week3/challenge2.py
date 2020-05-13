import requests
from bs4 import BeautifulSoup

# 1-3페이지 반복
for n in range(1, 4):
    raw = requests.get("https://news.ycombinator.com/news?p="+str(n),
                       headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("tr.athing")


    for ar in articles:
        rank = ar.select_one("span.rank").text
        title = ar.select_one("a.storylink").text
        if ar.select_one("span.sitestr") == None:
            source = ""
        else :
            source = ar.select_one("span.sitestr").text
        print(rank, title,source)
