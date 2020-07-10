#셀레니움 연습하기
from selenium import webdriver
import time

# 1.웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")
# 2. 네이버지도 접속하기
driver.get("https://v4.map.naver.com/")
# !!!추가//네이버 지도 업데이트 후 안내메시지 끄기##########
# 무시하고 진행해주세요.
driver.find_elements_by_css_selector("button.btn_close")[1].click()
##################################################


# 3. 검색창에 검색어 입력하기 // 검색창 : input#search-input
search_box = driver.find_element_by_css_selector("input#search-input")
search_box.send_keys("치킨")
# 4. 검색버튼 누르기 // 버튼 : button.spm
search_button = driver.find_element_by_css_selector("button.spm")
search_button.click()
# 5. 검색결과 확인하기

for n in range(1,20):
#지연시간 주기 ; 데이터를 가져오는데 시간이 걸림
    time.sleep(6)

    # 컨테이너 dl.lsnx_det
    # stores = html.select("dl.lsnx_det") 기존 html static
    stores = driver.find_elements_by_css_selector("dl.lsnx_det")

    # 가게이름 dt > a
    # 가게 주소 dd.addr
    # 전화번호 dd.tel
    for s in stores:
        name = s.find_element_by_css_selector("dt > a").text
        addr = s.find_element_by_css_selector("dd.addr").text
        # tel = s.find_elements_by_css_selector("dd.tel")
        # if tel:
        #     print(name, addr, tel[0].text)
        try:
            tel = s.find_elements_by_css_selector("dd.tel").text
        except:
            tel="전화번호 없음"
        print(name,addr, tel)
    # 페이지 버튼 div.paginate > *
    page_bar = driver.find_elements_by_css_selector("div.paginate > *")
    try:
        if n%5 != 0 :
            page_bar[n+1].click()
        else:
            page_bar[6].click()
    except:
        print("데이터 수집 완료")
        break
driver.close()


