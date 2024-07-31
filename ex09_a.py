# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON e depois crie novamente as instâncias da classe com os dados salvos
# Faça em arquivos separados.
import json


def dumpador(): #def para adiaar a execucao da funcaao e o usuario poder editar no json 
    #criando o arquivo JSON
    with open(ARQUIVO_PRINCIPAL, 'w', encoding='utf-8') as arquivo_teste:
        json.dump(resumo, arquivo_teste )


ARQUIVO_PRINCIPAL = 'testedoj.json'

class pessoa:
    def __init__(self, nome, cor_olhos, idade, porte_fisico):
        self.nome = nome 
        self.cor_olhos = cor_olhos 
        self.idade = idade
        self.porte_fisico = porte_fisico


pessoa1 = pessoa('Rafaela', 'azuis', 24, 'atletica')
pessoa2 = pessoa('Kleber', 'Castanhos', 31, 'robusto')
pessoa3 = pessoa('Jonas', 'Castanhos', 21, 'magro')
resumo = [vars(pessoa1), vars(pessoa2), vars(pessoa3)] #.__dict__ tambem poderia ser usado na frente do pessoa[i] em qualquer um dos tres que teria o mesmo resultdo





