def metade(preço):
    res = preço / 2
    return res


def dobro(preço):
    res = preço * 2
    return res


def aumentar(preço,taxa):
    res = (preço * 10 / 100) + preço
    return res

def diminuir(preço,taxa):
    res = preço - (preço * taxa / 100)
    return res
