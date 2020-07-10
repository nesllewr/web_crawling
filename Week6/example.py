# 네이버 검새겅 수집하기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import openpyxl

try :
    wb = openpyxl.load_workbook("naversearch.xlsx")
    sheet = wb.active
except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["순위","검색어"])
    # sheet.append(["순위","10대","20대","30대","40대","50대","전체 연령"])
driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.naver.com/")

first_setting = driver.find_element_by_css_selector("div#NM_RTK_ROLLING_WRAP")
first_setting.click()

search_setting = driver.find_elements_by_css_selector("a.range.NM_RTK_VIEW_filter_range")
for idx,v in enumerate(search_setting):
    if idx%5 == 0 :
        v.click()

age_button = driver.find_elements_by_css_selector("li.age_item")

for idx,v in enumerate(age_button):
    age_button[idx].click()
    sheet.append([age_button[idx].text])

    if idx == 0 :
        driver.find_element_by_css_selector("button#NM_RTK_VIEW_set_btn").click()
        time.sleep(1)
    # RTK_VIEW = driver.find_element_by_css_selector("div#NM_RTK_VIEW_list_wrap ").get_attribute("style")
    # if RTK_VIEW == "display: none;":
    search = driver.find_elements_by_css_selector("li.realtime_item > a.link_keyword > span.keyword")
    for i in range(10):
        # print(str(idx+1)+"위",search[idx].text)
        sheet.append([str(i+1)+"위",search[i].text])
    next_btn = driver.find_element_by_css_selector("a.tab.NM_RTK_VIEW_list_tab").click()
    search = driver.find_elements_by_css_selector("li.realtime_item > a.link_keyword > span.keyword")
    for i in range(10):
        # print(str(idx + 11 )+ "위", search[idx].text)
        sheet.append([str(i + 11 )+ "위", search[i].text])
    time.sleep(3)

driver.close()

wb.save("naversearch.xlsx")