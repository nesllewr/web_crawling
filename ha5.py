# import requests
# from bs4 import BeautifulSoup
#
# # 상영중 영화 페이지에 데이터를 요청
# raw = requests.get("http://ticket2.movie.daum.net/Movie/MovieRankList.aspx",
#                    headers={"User-Agent": "Mozilla/5.0"})
# html = BeautifulSoup(raw.text, 'html.parser')
#
# # 컨테이너 수집
import requests
from bs4 import BeautifulSoup

raw = requests.get("http://ticket2.movie.daum.net/Movie/MovieRankList.aspx",
                   headers={'User-Agent': 'Mozillo/5.0'})
html = BeautifulSoup(raw.text, 'html.parser')

movies = html.select("ul.list_boxthumb > li")

for movie in movies:
    title = movie.select_one("strong.tit_join > a")
    url = title.attrs['href']

    raw2 = requests.get(url,
                        headers={'User-Agent': 'Mozillo/5.0'})
    html2 = BeautifulSoup(raw2.text, 'html.parser')

    info = html2.select_one("div.movie_summary")
    title = info.select_one("strong.tit_movie")
    rating = info.select_one("em.emph_grade").text
    genre = info.select_one("dl.list_movie > dd:nth-of-type(1)").text
    director = info.select_one("dl.list_movie > dd.type_ellipsis >a").text

    print(title.text, rating, genre,director)
# movies = html.select("ul.list_boxthumb > li")
#
# # 수집한 컨테이너(영화) 반복하기
# for m in movies:
#
#     # 제목 수집해서 링크 저장하기
#     title = m.select_one("strong.tit_join > a")
#     url = title.attrs["href"]
#
#     # 상세페이지 데이터 요청하기
#     raw_each = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
#     html_each = BeautifulSoup(raw_each.text, 'html.parser')
#
#     # 제목, 평점, 장르, 감독, 배우 수집
#     title = html_each.select_one("strong.tit_movie").text
#     score = html_each.select_one("em.emph_grade").text
#
#     # dd 태그 안에 데이터를 순서로 구분
#     genre = html_each.select_one("dl.list_movie > dd:nth-of-type(1)").text
#     director = html_each.select("dl.list_movie > dd:nth-of-type(5) a")
#     actor = html_each.select("dl.list_movie > dd:nth-of-type(6) a")
#
#     print("제목:", title)
#     print("평점:", score)
#     print("장르:", genre)
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
