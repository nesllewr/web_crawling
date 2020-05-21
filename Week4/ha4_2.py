import requests
from bs4 import BeautifulSoup
import openpyxl

try:
    wb = openpyxl.load_workbook("daumnews.xlsx")
    sheet = wb.active
except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["제목","기사요약"])
    
for page in range(1, 4):
    raw = requests.get("https://search.daum.net/search?w=news&q=코알라&p="+str(page))
    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("div.wrap_cont")

    for ar in articles:
        title = ar.select_one("a.f_link_b").text
        summary = ar.select_one("p.f_eb.desc").text
        sheet.append([title, summary])

wb.save("daumnews.xlsx")