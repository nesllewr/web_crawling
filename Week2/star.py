print("LV1. 순서대로 별찍기(1,2,...,10)")
for i in range(10):
    print("*"*i)

print("LV2. 2단위로 별찍기(1,3,...,9)")
for i in range(1, 10, 2):
    print("*" * i)


print("LV3. 거꾸로로 별찍기(10,8,...,1)")
for i in range(10, 0, -1):
    print("*" * i)