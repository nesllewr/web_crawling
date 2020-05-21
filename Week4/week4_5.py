import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["제목", "채널명", "재생 수", "좋아요 수"])

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

# 3.반복하기
for cont in container :
    title = cont.select_one("dt.title").text.strip()
    chn = cont.select_one("dd.chn").text.strip()
    hit = cont.select_one("span.hit").text.strip()
    like = cont.select_one("span.like").text.strip()

    title = title.replace(",","")
    chn = chn.replace(",",'')
    hit = hit.replace(",",'')
    like = like.replace(",","")

    hit = hit.replace("재생 수","")
    like = like[5:]
    sheet.append([title, chn,hit,like])


wb.save("navertv.xlsx")