v = int(input('Qual é a velocidade atual do carro? '))
multa = (v - 80)*7
if v <=80:
    print('Tenham um bom dia! Dirigia com cuidado')
else:
    print('Multado! Você excedeu o limite permetido que é de 80KM/h' )
    print('Você deve pagar uma multa de R${: .2f}!'.format(multa))
    print('Tenham um bom dia! Dirigia com cuidado')