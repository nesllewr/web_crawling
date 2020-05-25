import requests
from bs4 import BeautifulSoup

from urllib.request import urlretrieve

raw = requests.get("https://m.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd",headers={"User-Agent": "Mozilla/5.0"})
html = BeautifulSoup(raw.text, "html.parser")

movies = html.select("div.media")
# 컨테이너를 반복하며 상세데이터(제목, 등급, 장르) 수집하기
for m in movies:
    title = m.select_one("span.h4:nth-of-type(2)")
    url = m.select_one("a").attrs["href"]

    raw_each = requests.get("https://m.imdb.com/"+url,headers={"User-Agent":"Mozilla/5.0"})
    html_each = BeautifulSoup(raw_each.text, "html.parser")

    poster = html_each.select_one("a.media-left img")
    src = poster.attrs["src"]
    urlretrieve(src, 'poster/' + title.text[:4] + '.png')


# # IMDb 홈페이지에 데이터 요청하기
# raw = requests.get("https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth",
#                    headers={"User-Agent": "Mozilla/5.0"})
# html = BeautifulSoup(raw.text, 'html.parser')
#
# # 컨테이너 수집하기
# movies = html.select("td.overview-top ")
#
# for m in movies:
#     title = m.select_one("h4 > a")
#
#     # 제목에서 링크 연결주소를 가져와 저장하기
#     url = title.attrs["href"]
#
#     # 상세페이지에 접속해서 데이터를 요청하기
#     raw_each = requests.get("https://www.imdb.com" + url, headers={"User-Agent": "Mozilla/5.0"})
#     html_each = BeautifulSoup(raw_each.text, 'html.parser')
#
#     # 포스터 데이터를 선택해서 src값 가져오기
#     # 포스터 선택자: div.poster img
#     poster = html_each.select_one("div.poster img")
#     src = poster.attrs["src"]
#
#     # urlretrieve 함수를 사용해서 이미지 저장하기
#     # poster 폴더 안에 이미지 저장하기
#     urlretrieve(src, 'poster/' + title.text[:4] + '.png')