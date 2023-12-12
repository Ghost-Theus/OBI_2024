# https://olimpiada.ic.unicamp.br/pratique/pj/2021/f1/plano/

x = int(input()) # Mb mensal
n = int(input()) # meses
mb_mensal = x * n
mb_usado = 0

for i in range(n):
    M = int(input())
    mb_usado += M

print(x + (mb_mensal - mb_usado))