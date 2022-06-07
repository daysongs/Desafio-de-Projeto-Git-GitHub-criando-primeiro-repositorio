from random import randint
from time import sleep
jogos = []
total = 0
print('=-'*30)
print(f"{'Jogar na mega sena':^50}")
print('=-'*30)
qt = int(input('Qauntos jogos Você quer que eu sortei: '))
while total <= qt:
    cont = 0
    while True:
        n = randint(1,25)
        if n not in jogos:
            jogos.append(n)
            cont += 1
        if cont >= 15:
            break
    jogos.sort()
    total += 1
    sleep(1)
    print(f'Jogo {total}: {jogos}')
    jogos.clear()