def fatorial(n,show=False):
    """
    → Calcula o fatorial de um número
    :param n: número a ser calculado
    :param show: opicinal mostra ou não a conta
    :return: o fatorial de n
    """
    fat = 1
    for c in range(n,0,-1):
        if show:
            print(c,end=' ')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        fat *= c
    return fat


#programa principal
print(fatorial(5,False))
help(fatorial)
