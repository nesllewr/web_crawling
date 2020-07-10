from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://maps.google.com")

# 카페 정보 수집
# 1. 가게이름
# 2. 평점
# 3. 주소
# 4. 카페정보 100개(5페이지 수집하기)

searchbox = driver.find_element_by_css_selector("input#searchboxinput")
searchbox.send_keys("카페")

search_btn = driver.find_element_by_css_selector("button#searchbox-searchbutton")
search_btn.click()

for n in range(0,5):
    time.sleep(7)

    cafes = driver.find_elements_by_css_selector("div.section-result-content")

    for cafe in cafes :
        name = cafe.find_element_by_css_selector("h3 > span:nth-of-type(1)").text
        try:
            rate = cafe.find_element_by_css_selector("span.cards-rating-score").text
        except:
            rate="평점없음"
        addr = cafe.find_element_by_css_selector("div.section-result-details-container").text
        print(name,rate,addr)

    page_btn = driver.find_element_by_css_selector("span.n7lv7yjyC35__button-next-icon")
    try:
        page_btn.click()
    except:
        print("데이터 수집 완료")
        break