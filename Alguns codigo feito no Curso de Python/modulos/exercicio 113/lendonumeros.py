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


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(KeyboardInterrupt):
            print('\033[31mEntradas de dados interrompida pelo usuario\033[m')
            return 0
        except(TypeError, ValueError):
            print('\033[31mO valor informado é invalido\033[m')
            continue
        else:
            return n


# programa principal
num = leiaint('Digite um valor inteiro: ')
rnum = leiafloat('Digite um número real: ')
print(f'Você digitou o valor {num} e o real {rnum}')
