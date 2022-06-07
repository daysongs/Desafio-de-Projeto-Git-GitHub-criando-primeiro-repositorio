def leiaint(msg):
    n = input(msg)
    while not n.isnumeric():
        if not n.isnumeric():
            print('\33[31mERRO!!! Digite um número validoe.\33[m')
        n = input(msg)
    n = int(n)
    return n


#programa principal
a = leiaint('Digite um número: ')
print(f' Você digitou o número {a}')