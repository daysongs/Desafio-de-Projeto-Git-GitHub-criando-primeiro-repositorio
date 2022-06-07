matriz = [[0,0,0], [0,0,0],[0,0,0]]
somap = somac = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para {l}, {c}: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end='')
        if matriz[l][c] % 2 == 0 :
            somap += matriz[l][c]
    print()
print('=-'*30)
print(f' A soma dos valores pares é: {somap}')
for l in range(0,3):
    somac += matriz[l][2]
print(f'A soma da 3ª coluna é: {somac}')
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior elemento da linha 2 é: {maior}')
