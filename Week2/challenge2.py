data = ["조회수: 1,500", "조회수: 1,002", "조회수: 300", "조회수: 251",
        "조회수: 13,432", "조회수: 998"]
sum =0

print("LV1. 리스트 안에 있는 데이터 출력하기")
for i in data:
    print(i)
    
print("LV2. 리스트 안에 있는 데이터에서 숫자만 추출하기")
for i in range(len(data)):
    print(int(data[i][5:].replace(",","")))

print("LV3. 조회수 총 합 구하기")
for i in range(len(data)):
    sum += int(data[i][5:].replace(",",""))
print("총 합: "+ str(sum))
