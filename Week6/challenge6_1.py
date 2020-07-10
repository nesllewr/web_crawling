from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://papago.naver.com")

time.sleep(1)

trans = driver.find_element_by_css_selector("textarea#txtSource")
trans.send_keys("seize the day")
trans_btn = driver.find_element_by_css_selector("button#btnTranslate")
trans_btn.click()
time.sleep(1)
result = driver.find_element_by_css_selector("div#txtTarget").text
print(result)

# driver.close()
#
# from selenium import webdriver
# import time
#
# # 크롬창(웹드라이버) 열기
# driver = webdriver.Chrome("./chromedriver")
#
# # 파파고 페이지 접속
# driver.get("https://papago.naver.com")
#
# # 페이지 접속 후 시간 지연
# time.sleep(0.5)
#
# # 입력창에 검색어 입력
# input_box = driver.find_element_by_css_selector("textarea#txtSource")
# input_box.send_keys("seize the day")
#
# # 번역 버튼 클릭
# button = driver.find_element_by_css_selector("button#btnTranslate")
# button.click()
#
# # 버튼 클릭 후 시간 지연 & 검색결과 출력
# time.sleep(0.5)
# result = driver.find_element_by_css_selector("div#txtTarget").text
# print(result)
#
# # 크롬창 닫기
# # driver.close()