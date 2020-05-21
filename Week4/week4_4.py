# openpyxl 연습하기

import openpyxl

wb = openpyxl.Workbook()
# 현재 활성화된 엑셀파일 sheet
sheet = wb.active

sheet['A1'] = "Hello World"
sheet.cell(row=3, column=3).value = "Good Bye"

# 행의 마지막에 행별로 데이터를 저장해줌
sheet.append(["Python","Java", "HTML", "JAVASCRIPT"])


wb.save("test.xlsx")


