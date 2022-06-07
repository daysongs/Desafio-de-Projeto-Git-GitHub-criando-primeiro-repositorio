def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuario\033[n')
            return 0
        except (ValueError, TypeError):
            print(f'\033[31mERRO!! não é um valor valido\033[m')
            continue
        else:
            return n



def linha(tam=42):
    return '-' * tam


def cabeçario(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçario('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[34m{item}\033[m')
        c += 1
    print(linha())
    op = leiaint('\033[32mSua opção: \033[m')
    return op