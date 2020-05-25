import requests
from bs4 import BeautifulSoup

raw = requests.get("https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd",headers={'User-Agent':'Mozilla/5.0'})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 수집하기
# movies = html.select("span.media-body.media-vertical-align.lister-item-content")
movies = html.select("div.lister-item-content")
# 컨테이너를 반복하며 상세데이터(제목, 등급, 장르) 수집하기
for m in movies:
    title = m.select_one("h3 > a").text.strip("\n")
    print("제목 :",title)
    genre_all = m.select_one("span.genre").text.strip("\n")
    print("장르 :",genre_all)
    director = m.select_one("p.text-muted.text-small > a:nth-of-type(2)").text
    print("감독 :", director)
    actor = m.select_one("p.text-muted.text-small").text
    print("배우:", actor)
    print("="*50)



# raw = requests.get("https://m.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd",headers={'User-Agent':'Mozilla/5.0'})
# html = BeautifulSoup(raw.text, 'html.parser')
#
# # 컨테이너 수집하기
# # movies = html.select("span.media-body.media-vertical-align.lister-item-content")
# movies = html.select("div.media")
# # 컨테이너를 반복하며 상세데이터(제목, 등급, 장르) 수집하기
# for m in movies:
#     title = m.select_one("span.h4:nth-of-type(2)").text
#     print("제목 :",title)
#     rate_all = m.select_one("span.certificate")
#     if rate_all != None:
#         rate_all = rate_all.text
#         print("등급 :",rate_all)
#     genre_all = m.select_one("span.genre").text.strip("\n")
#     print("장르 :",genre_all)
#     print("="*50)



    # import requests
    # from bs4 import BeautifulSoup
    #
    # # IMDb 홈페이지에 데이터 요청하기
    # raw = requests.get("https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth",
    #                    headers={"User-Agent": "Mozilla/5.0"})
    # html = BeautifulSoup(raw.text, 'html.parser')
    #
    # # 컨테이너 수집하기
    # movies = html.select("td.overview-top ")
    #
    # # 컨테이너를 반복하며 상세데이터(제목, 감독, 배우) 수집하기
    # for m in movies:
    #     title = m.select_one("h4 > a").text
    #
    #     # 감독, 배우는 여러명일 수 있으므로 select를 활용해서 리스트로 저장합니다.
    #     # 원하는 데이터가 컨테이너의 자식관계에 있을 때는 자식 선택자(>)를 먼저 써줄 수도 있습니다.
    #     director = m.select("> div:nth-of-type(3) a")
    #     actor = m.select("> div:nth-of-type(4) a")
    #
    #     #############################################
    #     # 추가
    #
    #     # 장르 데이터를 가지고 있는 태그를 선택합니다.
    #     genre_all = m.select_one("p.cert-runtime-genre").text
    #
    #     # Action이라는 키워드가 포함되어있지 않은 경우 출력하지 않고 스킵합니다.
    #     if "Action" not in genre_all:
    #         continue
    #     #############################################
    #
    #     print("제목:", title)
    #     # print(score)
    #
    #     print("감독:")
    #     for d in director:
    #         print(d.text)
    #
    #     print("배우:")
    #     for a in actor:
    #         print(a.text)
    #
    #     print("=" * 50)