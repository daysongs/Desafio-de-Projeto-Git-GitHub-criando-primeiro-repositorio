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
