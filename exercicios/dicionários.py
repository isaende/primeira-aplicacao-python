# Exercício 01
informacoes = [{
    'nome':'Frederico',
    'idade':2,
    'cidade':'Diadema',
    }]

# Exercício 02
informacoes['idade'] = 20
informacoes['profissão'] = 'Desempregado'
del informacoes['cidade']

# Exercício 03
if 'nome' in informacoes:
    print(f'A chave {'nome'} existe dentro desse dicionário')
else:
    print(f'A chave {'nome'} não existe dentro desse dicionário')