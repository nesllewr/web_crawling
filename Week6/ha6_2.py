from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.instagram.com/explore/tags/ootd/")

id = "01024026131"
password ="ska787813z"

# 컨테이너(포스트) 12개 저장
instagram = driver.find_elements_by_css_selector("div._9AhH0")
instagram[0].click()
time.sleep(1)
inputs = driver.find_elements_by_css_selector("input._2hvTZ.pexuQ.zyHYP")
inputs[0].send_keys(id)
inputs[1].send_keys(password)

login_btn = driver.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF > div.Igw0E.IwRSH.eGOV_._4EzTm")
login_btn.click()

time.sleep(3)
instagram = driver.find_elements_by_css_selector("div._9AhH0")

# 컨테이너 반복하기
for insta in instagram[:12]:
    # 포스트 클릭하기
    insta.click()
    # 시간 지연
    time.sleep(3)
    # 본문 선택 후 출력
    post = driver.find_element_by_css_selector("div.C4VMK span").text
    print(post)

    # 닫기 버튼 클릭
    but_close = driver.find_element_by_css_selector("div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG")
    but_close.click()

#
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# element = WebDriverWait(driver, 5).until(
# EC.presence_of_element_located( (By.CLASS_NAME, 'class_name')))