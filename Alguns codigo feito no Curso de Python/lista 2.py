from math import sqrt
print('Para Calcular a distância entre dois pontos digite: ')
x1 = float(input('A cordenada x do primeiro ponto: '))
y1 = float(input('A cordenada y do primeiro ponto: '))
x2 = float(input('A cordenada x do segundo ponto:  '))
y2 = float(input('A cordenada y do segundo ponto'))
dp = sqrt((x1 - x2)**2 + (y1 - y2)**2)
if dp >= 10:
    print('longe')
else:
    print('perto')