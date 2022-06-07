from ex115.lib.interface import *
from ex115.lib.arquivo import *
from  time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExite(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar pessoa','Sair do sitema'])
    if resposta == 1:
        # opeção de lista um conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2 :
        #opção de cadastra uma nova pessoa
        cabeçario('Novo Cadastro')
        nome = str(input('Nome: ')).strip()
        idade = leiaint('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabeçario('Saindo do sistema.. até logo')
        break
    else:
        print('\033[31mOpeção invalida tente novamente\033[m')
    sleep(2)
