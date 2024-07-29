# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON e depois crie novamente as instâncias da classe com os dados salvos
# Faça em arquivos separados.
import json

class pessoa:
    def __init__(self, nome, cor_olhos, idade, porte_fisico):
        self.nome = nome 
        self.cor_olhos = cor_olhos 
        self.idade = idade
        self.porte_fisico = porte_fisico


pessoa1 = pessoa('Ana', 'azuis', 24, 'atletica')
pessoa2 = pessoa('Kleber', 'Castanhos', 31, 'robusto')
#criando o arquivo
with open('C:\\Users\\Luis\\Downloads\\dados_pessoa.json', 'w', encoding='utf-8') as arquivo_teste:
        json.dump(pessoa1.__dict__, arquivo_teste)
        json.dump(pessoa2.__dict__, arquivo_teste)


