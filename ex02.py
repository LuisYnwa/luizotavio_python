#EXPLICAÇÃO
def criar_multiplicador(multiplicador):
    def multiplicar(numero): #número será o valor inserido do usuário
        return numero * multiplicador #como a ordem dos fatores não altera o produto, você pode juntar o valor definido na função com o do usuário
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2)) #já aqui ele utilizará o argumento "número", sem a necessidade da criação de condicionais 
print(triplicar(2))
print(quadruplicar(2))