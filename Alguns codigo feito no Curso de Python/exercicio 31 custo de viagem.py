distancia = float(input('Qual a distancia da viagem? '))
print('Você esta preste a começar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    print('Sua viagem vai custar R${:.2f}'.format(distancia*0.50))
else:
    print('Sua viagem vai custar R${:.2f}'.format(distancia*0.45))