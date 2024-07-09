lista_final = []
lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4, 5, 6]
def somador(L1, L2):
    intervalo = min(len(L1), len(L2))
    for i in range(intervalo):
        lista_final.append(lista1[i] + lista2[i])
    return lista_final

print(somador(lista1, lista2)) 

#metodo usando as funcoes ja presentes no python:
lista_final = [x + y for x, y in zip(lista1, lista2)]
print(lista_final)