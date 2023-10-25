# copy, sorted, produtos.sort(mexer dentro da lista)
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda) com os 10%

# Ordene os produtos por nome decrescente (do maior para menor) (SORT OU SORTED(para não encostar na lista))
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy

produtos = [
    {'nome': 'Melancia', 'preco': 10.00},
    {'nome': 'Pizza', 'preco': 22.32},
    {'nome': 'Banana', 'preco': 10.11},
    {'nome': 'Abacaxi', 'preco': 105.87},
    {'nome': 'Amora', 'preco': 69.90},
]

preco_alterado = [
    {**produ, 'preco': round(produ ['preco'] * 1.10, 2)}
    for produ in produtos
]
#fazer uma cópia da lista sem módulo antes de tudo 

produtos_ordenados_nome = sorted (preco_alterado, key=lambda n: n['nome'], reverse=True)
produtos_ordenados_preco = sorted (preco_alterado, key=lambda n: n['preco'])

print(f'ALTERAÇÃO DE PREÇOS: {preco_alterado}')
print(f'ORDENAÇÃO POR NOME: {produtos_ordenados_nome}')
print(f'ORDENAÇÃO POR PREÇO: {produtos_ordenados_preco}')