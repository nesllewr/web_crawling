# 네이버 영화 데이터 수집

import requests
from bs4 import BeautifulSoup

# 웹페이지에서 소스코드를 가져와 BeautifulSoup으로 파싱
raw = requests.get("https://movie.naver.com/movie/running/current.nhn",
                   headers={'User-Agent':'Mozilla/5.0'})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 dl.lst_dsc
movies = html.select("dl.lst_dsc")

for m in movies:
    # 제목 dl.tit > a
    title = m.select_one("dt.tit > a").text
    # 평점 div.star_t1 a span.num
    score = m.select_one("div.star_t1 a span.num").text
    # 장르 dl.lst_dsc dl.info_txt1 dd a
    # 감독 dl.lst_dsc dl.info_txt1 dd a
    # 배우 dl.lst_dsc dl.info_txt1 dd a

    # # select 함수를 이용하는 방법
    # info = m.select("dd") # 리스트 형태로 담긴다.
    # # info = m.select("dl.info_txt1 dd")  # 이미 컨테이너를 가져 옴
    #
    # genre = info[0].select("a") # 영화 하나가 여러가지 장르를 가짐
    # director = info[1].select("a")  # 영화 하나가 여러가지 장르를 가짐
    # actor = info[2].select("a")  # 영화 하나가 여러가지 장르를 가짐

    # # 값이 없는 경우 에러가 나기 때문에 try except문 사용필요

    # 선택자를 사용하는 방법 " 태그이름름nth-of-type(숫자)"
    genre = m.select("dl.info_txt1 dd:nth-of-type(1) a")
    director = m.select("dl.info_txt1 dd:nth-of-type(2) a")
    actor = m.select("dl.info_txt1 dd:nth-of-type(3) a")
    # 해당하는 선택자가 없다면 비어있는 리스트

    if float(score) < 8.5 :
        continue
    # continue는 밑의 내용을 skip

    genre_all = m.select_one("dl.info_txt1 dd:nth-of-type(1) span.link_txt")
    # if genre_all != None and "액션" not in genre_all.text:
    #     continue

    # print(title)
    # print("-"*50)
    # print(score)
    # print("-"*50)
    #
    # for g in genre:
    #     print(g.text)
    # print("-"*50)
    # for a in actor:
    #     print(a.text)
    # print("-"*50)


