line = input("생년울일을 6자리로 입력해주세요.(yymmdd) : ")
print("----------------------------------------------")
print("당신의 생일은 {}년{}월{}일입니다.".format(line[:2],line[2:4],line[4:6]))