galera = []
dados = []
maior = menor = 0
for c in range(0,3): #esse bloco adicina elementos na lista dados dps faz uma copia para lista galera e exclui a lista dados
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera: # esse bloco printa nomes e idade da lista galera
    print(f'{p[0]} tem {p[1]} anos')
for i in galera: # esse bloco diz quem é maior e menor de idade e quantos são maoiores ou menores de idade
    if i[1] > 18:
        print(f'{i[0]} é maior de idade')
        maior += 1
    else:
        print(f'{i[0]} é menor de idade')
        menor += 1
print(f'temos {maior} maiores e {menor} menores de idade')
