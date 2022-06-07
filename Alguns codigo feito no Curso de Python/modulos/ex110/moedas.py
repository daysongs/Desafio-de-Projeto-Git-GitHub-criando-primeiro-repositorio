def metade(preço=0,formatar=False):
    res = preço / 2
    return res if formatar is False else moeda(res)


def dobro(preço=0,formatar=False):
    res = preço * 2
    return res if formatar is False else moeda(res)


def aumentar(preço=0,taxa=0,formatar=False):
    res = (preço * taxa / 100) + preço
    return res if formatar is False else moeda(res)

def diminuir(preço=0,taxa=0,formatar=False):
    res = preço - (preço * taxa / 100)
    return res if formatar is False else moeda(res)

def moeda(preço=0,moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')

def resposta(preço=0,taxaa=0,taxar=0):
    print('-'*30)
    print('Analizando o Preço'.center(30))
    print('-'*30)
    print(f'Preço analizado      \t{moeda(preço)}')
    print(f'A metdade do preço é \t{metade(preço,True)}')
    print(f'O dobro do preço é   \t{dobro(preço,True)}')
    print(f'Com {taxaa} de aumento é \t{aumentar(preço,taxaa,True)}')
    print(f'Com {taxar} de desconto é \t{diminuir(preço,taxar,True)}')

