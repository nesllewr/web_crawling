import requests
from bs4 import BeautifulSoup

f = open("movieranking.csv",'w',encoding='UTF-8')
f.write("순위,영화 제목, 평점\n")

raw = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=20200511", headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
html = BeautifulSoup(raw.text, 'html.parser')
movies = html.select("tbody > tr")
num = 0 ; sumpoint = 0.00
for m in movies:
    rank = m.select_one('td.ac > img')
    title = m.select_one('div.tit5')
    point = m.select_one('td.point')
    if rank != None:
        rank = rank.attrs['alt']
        title = title.text.strip("\n")
        point = point.text
        f.write(rank+","+title + "," + point+'\n')
        point = float(point)
        sumpoint += point
        num += 1


f.write("평균 별점 : "+str(round((sumpoint/num),2))+"\n")
f.close()