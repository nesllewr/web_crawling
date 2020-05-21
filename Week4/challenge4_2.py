import requests
from bs4 import BeautifulSoup
import openpyxl

try :
    wb = openpyxl.load_workbook("navernews.xlsx")
    sheet = wb.active
except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["검색어","기사제목", "언론사"])


# 컨테이너 : ul
# 기사제목 : a._sp_each_title
# 언론사 : span._sp_each_source


keyword = input("검색어를 입려해주세요 : ")

# 여러 페이지에서 수집되는 수집기
for n in range(1, 100, 10) :
    raw = requests.get(
        "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="+keyword+"&start=" + str(n),
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
    html = BeautifulSoup(raw.text, 'html.parser')
    articles = html.select("ul.type01 > li")

    for ar in articles:
        title = ar.select_one('a._sp_each_title').text.replace(",","")
        source = ar.select_one('span._sp_each_source').text.replace(',','')

        sheet.append([keyword, title,source])

wb.save("navernews.xlsx")