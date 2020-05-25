pay = input("시급을 입력해주세요: ")
pay = int(pay)

if pay > 8350 :
    print("적절한 시급입니다 :)")
else :
    print("최저 임금보다 작아요 :(")

numbers = [1 , 3, 5, 6, 8, 9, 10]

for n in numbers:
    if (n >= 5) and (n < 3) :
        print(n)

articles = ["손흥민은 손으로 상대의 얼굴을 밀며 맞받아쳤다.",
            "AS로마의 니콜로 자니올로",
            "이강인의 팀 동료 페란 토레스"]

for a in articles:
    if "손흥민" in a:
        print("손흥민이 나오는 기사")
    elif "이강인" in a:
        print("이강인이 나오는 기사")
    elif "니올로" in a:
        print(1)
    else :
        print("손흥민/이강인이 나오지 않는 기사")

players = ["손흥민", "이강인", "케빈하르", "백승호", "황의조"]

if "손흥민" in players:
    print(1)