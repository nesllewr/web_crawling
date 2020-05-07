players = ["황의조","황의찬","구자철","이재성","기성용"]

for i in players:
    print(i)
print("--------------------------------")

idx = int(input("OUT 시킬 선수 번호 : "))
name = input("IN할 선수 이름 : ")

del players[idx]
players.append(name)

print("---------------------------------")
for i in players :
    print(i)
