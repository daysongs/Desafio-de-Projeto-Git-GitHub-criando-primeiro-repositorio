largura=float(input('Digite a largura'))
altura=float(input('Digite a altura'))
area= largura * altura
tinta= area/2
print('sua parede tem a dimensão de {}mx{}m e sua area é de {}m² '.format(largura, altura, area))
print('Para pintar essa parede você precisará de {}l de tinta'.format(tinta))