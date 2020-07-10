from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")

# 네이버 로그인
driver.get("https://nid.naver.com")
id = "dklasdjfklasdjf"
password ="ㄴㅁㄹㄴㅇㄹㅇㄻㄹ"
# 아이디 입력
input_id = driver.find_element_by_css_selector("input#id")
input_id.send_keys(id)

# 비밀번호 입력
input_password = driver.find_element_by_css_selector("input#pw")
input_password.send_keys(password)

# 로그인 버튼 클릭
login = driver.find_element_by_css_selector("input.btn_global")
login.click()



#페이스북 로그인 코드
from selenium import webdriver

# # 계정정보 입력
# id = "아이"
# password = "비밀번호"
#
# # 크롬창(웹드라이버) 열기
# driver = webdriver.Chrome("./chromedriver")
#
# # 페이스북 메인 페이지 접속
# driver.get("https://facebook.com")
#
#
# # 아이디 입력
# input_id = driver.find_element_by_css_selector("input#email")
# input_id.send_keys(id)
#
# # 비밀번호 입력
# input_password = driver.find_element_by_css_selector("input#pass")
# input_password.send_keys(password)
#
# # 로그인 버튼 클릭
# login = driver.find_element_by_css_selector("input#u_0_e")
# login.click()
