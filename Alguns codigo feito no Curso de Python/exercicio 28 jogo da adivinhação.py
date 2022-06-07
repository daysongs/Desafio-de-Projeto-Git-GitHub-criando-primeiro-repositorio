import random
import time
computador = random.randint(0,5) #faz o computador penssar
print('-=- '*20)
print('vou pensar em um número entere 0 e 5. Tente adivinhar.')
print('-=- '*20)
n = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
print('PROCESSANSDO')
time.sleep(3) # da um atraso de 3 segundos na respota
if n== computador :
    print('Parabens você ganhou pensei exatamente neste número {} !'.format(computador))
else:
    print('Ganhei! pensei no número {} e não no {} !'.format(computador, n))