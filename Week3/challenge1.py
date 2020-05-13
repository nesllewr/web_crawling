import requests
from bs4 import BeautifulSoup

raw = requests.get("https://tv.naver.com/r")
html = BeautifulSoup(raw.text, "html.parser")

# 1위 - 3위 컨테이너 선택자: div.inner
clips = html.select("div.inner")

for cl in clips:
    title = cl.select_one("dt.title")
    chn = cl.select_one("dd.chn")
    hit = cl.select_one("span.hit")
    like = cl.select_one("span.like")

    print("제목", title.text.strip())
    print("채널명", chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("="*50)


# 4위-100위 컨테이너 선택자:
clips = html.select("div.cds")

for cl in clips:
    title = cl.select_one("dt.title")
    chn = cl.select_one("dd.chn")
    hit = cl.select_one("span.hit")
    like = cl.select_one("span.like")

    print("제목", title.text.strip())
    print("채널명", chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("="*50)

################################
# 1~100위를 한번에 선택할 수 있는 선택자로 찾을 경우

raw = requests.get("https://tv.naver.com/r")
html = BeautifulSoup(raw.text, "html.parser")

# 1위 - 100위 컨테이너 선택자: dl.cds_info
clips = html.select("dl.cds_info")

for cl in clips:
    title = cl.select_one("dt.title")
    chn = cl.select_one("dd.chn")
    hit = cl.select_one("span.hit")
    like = cl.select_one("span.like")

    print("제목", title.text.strip())
    print("채널명", chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("="*50)
