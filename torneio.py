# https://olimpiada.ic.unicamp.br/pratique/pj/2021/f1/torneio/

v = 0

for i in range(6):
    res = input()
    if res == "V":
        v += 1

if v == 5 or v == 6:
    print("1")
elif v == 3 or v == 4:
    print("2")
elif v == 1 or v == 2:
    print("3")
else:
    print("-1")
