def area(largua,comp):
    a = largua * comp
    print(f'A area de um terreno com {largua}m de largura e {comp}m de comprimento é {a:.2f}m²')


# progama principal
print('Controle de terreno')
print('=-'*20)
l = float(input('Digite a laragura do seu terreno (m): '))
c = float(input('Digite a larguara do seu terreno (m): '))
area(l,c)