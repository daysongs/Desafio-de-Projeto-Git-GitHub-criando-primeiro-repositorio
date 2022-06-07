def notas(*n,sit=False):
    """
    → Função para analizar notas e situações de vario alunos
    :param n:uma ou mais notas de aluno
    :param sit:opicinal: define a situação da turma
    :return:um dicionario com o: total de noatas cadastradas, maior nota,
    menor nota, media das notas cadastrada, se sit=True tbm mostra a situação de
    acordo com a média podendo ela ser: ruim razoavel ou boa.
    """
    r = {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n) / len(n)
    if sit:
        if r['Media'] < 5:
            r['Situação'] = 'Ruim'
        elif 5 <= r['Media'] < 7:
            r['Situação'] = 'Razoavel'
        else:
            r['Situação'] = 'Boa'
    return r


#programa principal
resp = notas(5.6,7,8,9,sit=True)
print(resp)

