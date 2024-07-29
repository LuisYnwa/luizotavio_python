#lendo a base de dados JSON

import json

with open('C:\\Users\\Luis\\Downloads\\dados_pessoa.json', 'r') as arquivo_teste:
    dados_fisicos = json.load(arquivo_teste)
    dados_finais = dados_fisicos(**dados_fisicos)

print(f'Nome: {dados_finais.nome}')
print(f'Idade: {dados_finais.idade}')
print(f'Porte fisico: {dados_finais.porte_fisico}')
print(f'Cor dos olhos: {dados_finais.cor_olhos}')
