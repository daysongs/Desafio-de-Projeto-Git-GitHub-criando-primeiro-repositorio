lista = ('lapis',3,
         'caneta',2,
         'celular',500,
         'calça',45.20)
for pos in range(0,len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R${lista[pos]:.2f}')