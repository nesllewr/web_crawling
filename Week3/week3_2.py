import requests
from bs4 import BeautifulSoup

raw = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%BD%94%EC%95%8C%EB%9D%BC", headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 : ul
# 기사제목 : a._sp_each_title
# 언론사 : span._sp_each_source

# 1.컨테이너 수빕
articles = html.select("ul.type01 > li")

# 2. 기사데이터 수빕
title = articles[0].select_one('a._sp_each_title').text
source = articles[0].select_one('span._sp_each_source').text

print(title,source)

# 3. 수집 반복
for ar in articles :
    title = ar.select_one('a._sp_each_title').text
    source = ar.select_one('span._sp_each_source').text

    print(title,source)

# 여러 페이지에서 수집되는 수집기
for n in range(1, 100, 10) :
    raw = requests.get(
        "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%BD%94%EC%95%8C%EB%9D%BC&start=" + str(n),
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
    html = BeautifulSoup(raw.text, 'html.parser')
    articles = html.select("ul.type01 > li")

    for ar in articles:
        title = ar.select_one('a._sp_each_title').text
        source = ar.select_one('span._sp_each_source').text

        print(title, source)
