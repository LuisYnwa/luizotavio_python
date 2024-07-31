#lendo a base de dados JSON
import json
from ex09_a import ARQUIVO_PRINCIPAL, pessoa, dumpador, resumo

dumpador()
with open(ARQUIVO_PRINCIPAL, 'r') as arquivo_teste:
    dados_fisicos = json.load(arquivo_teste)
    p1 = pessoa(**dados_fisicos[0])
    p2 = pessoa(**dados_fisicos[1])
    p3 = pessoa(**dados_fisicos[2])

    print(p1.nome, p1.idade, p1.cor_olhos, p1.porte_fisico)
    print(p2.nome, p2.idade, p2.cor_olhos, p2.porte_fisico)
    print(p3.nome, p3.idade, p3.cor_olhos, p3.porte_fisico)
    #nomes, idades etc se conectaando diretamente com a classe definida no arquivo anterior 


