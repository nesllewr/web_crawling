# urllib에서 urlretrieve 가져오기
from urllib.request import urlretrieve
# 에러 발생하는 경우 붙여넣기
# import ssl
#
# ssl._create_default_https_context = ssl._create_unverified_context
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
    title = m.select_one("dt.tit > a")
    # <a href="/movie/bi/mi/basic.nhn?code=191633">트롤: 월드 투어</a>
    url = title.attrs["href"]
    print("="*50)
    print(title.text)

    each_raw = requests.get("https://movie.naver.com/"+url, headers={'User-Agent':'Mozilla/5.0'})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    # 컨테이너 div.score_result > ul > li
    # 평점 div.star_score em
    # 리뷰 div.score_reple p

    reviews = each_html.select("div.score_result > ul > li")
    print("-"*50)
    for r in reviews:
        stars = r.select_one("div.star_score em").text
        reple = r.select_one("div.score_reple p").text
        print(stars, reple)

    # 포스터 선택자 : div.mv_info_area div.poster img
    poster = each_html.select_one("div.mv_info_area div.poster img")
    poster_src = poster.attrs["src"]
    # print(poster_src)

    urlretrieve(poster_src,"poster/"+title.text[:2]+".png")