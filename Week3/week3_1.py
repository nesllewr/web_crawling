import requests
from bs4 import BeautifulSoup

#request안의 get함수를 통해 홈페이지 데이터 저장
raw = requests.get("https://tv.naver.com/r")
# print(raw.text)
#parsing을 통해 선택자를 가져올 수 있다.
html = BeautifulSoup(raw.text, 'html.parser')
# print(html)

# 1~3위 컨테이너 : div.inner
# 제목 : dt.title
# 채널 : dd.chn
# 재생수 : span.hit
# 좋아요 : span.like

# 1. 컨테이너 수집
container = html.select("div.inner")
print(container)
# 대괄호 안에 있음 -> 리스트 형식으로 저장

# 2. 영상데이터 수집
title = container[0].select_one("dt.title")
print(title.text)
#select는 인덱싱으로 원하는 걸 뽑지만
# select_one은 해당하는 것중 가장 먼저 있는 데이터를 가져옴

chn = container[0].select_one("dd.chn")
hit = container[0].select_one("span.hit")
like = container[0].select_one("span.like")

# 3.반복하기
for cont in container :
    title = container[0].select_one("dt.title")
    chn = container[0].select_one("dd.chn")
    hit = container[0].select_one("span.hit")
    like = container[0].select_one("span.like")

    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
