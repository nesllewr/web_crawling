import requests
from bs4 import BeautifulSoup

f = open("naverseries.csv","w",encoding="UTF-8")
f.write("제목, 저자\n")
for p in range(1, 6):
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(p),
                       headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    books = html.select("div.lst_thum_wrap li")
    for b in books:
        title = b.select_one("a strong").text.replace(",","")
        author = b.select_one("span.writer").text.replace(",","")

        f.write(title+","+author+"\n")

# raw = requests.get("https://www.youtube.com/feed/trending", headers={
#             'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
# html = BeautifulSoup(raw.text, 'html.parser')
#
# clips = html.select("div.text-wrapper style-scope ytd-video-renderer")
# print(clips)

f.close()