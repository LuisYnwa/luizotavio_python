#INCOMPLETO
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'PR']
def zipper(a, b):
    
    zipado = dict(zip(a, b)) #zip, funcao antiva do python que une duas listas e a organiza automaticamente a partir da menor entre elas
    #use a funcao "zip_tools" da library "itertools" quando quiser fazer o mesmo acima porem pegando a lista com o maior comprimento
    return zipado

final = zipper(cidades, estados)
print(final)

#funcao sendo feita abaixo de forma logica:
#def zipper(L1, L2):
    #intervalo = min(len(L1), len(L2))
    #return [(L1[i], L2[i]) for i in range(intervalo)]

#l1 = ['Salvador', 'BA', 'Ubatuba']
#l2 = ['BA', 'SP', 'MG', 'RJ']

#print(zipper(l1, l2)) 