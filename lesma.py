a = int(input())  # altura do muro
s = int(input())  # distância que ela sobe por dia
d = int(input())  # distância que ela desce por noite

qA = 0 #qntd atual
dias = 0

while qA < a:
    qA += s 
    dias += 1
    if qA >= a:
        break
    qA -= d

print(dias)
