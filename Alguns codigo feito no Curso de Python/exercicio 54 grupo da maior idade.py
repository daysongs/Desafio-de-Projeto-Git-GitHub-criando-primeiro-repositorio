from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pess in range(1,8):
    nas = int(input(' Em que ano {}ª nasceu?'.format(pess)))
    idade = atual - nas
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print(' Ao todo tivemos {} maiores de idade'.format(totalmaior))
print('E {} menores de idade'.format(totalmenor))

