lista_tarefas = []
lista_desfeitos = []
print('Listar / Desfazer / Refazer / Sair')
while True:
    usuario = input('Digite um comando ou tarefa: ').upper()
    try:
        if usuario in ['LISTAR', 'DESFAZER', 'REFAZER'] and lista_tarefas == []:
            print('A lista esta vazia!!')

        elif usuario == 'LISTAR':
            for a, b in enumerate(lista_tarefas, 1):
                print(f'{a} - {b}')

        
        elif usuario == 'DESFAZER':
            tarefa_desfeita = lista_tarefas.pop()
            lista_desfeitos.append(tarefa_desfeita)

        elif usuario == 'REFAZER':
            tarefa_refeita = lista_desfeitos.pop()
            lista_tarefas.append(tarefa_refeita)

        elif usuario == 'SAIR':
            print('Lista de Tarefas Salva com sucesso!')
            with open('C:\\Users\\Luis\\Downloads\\lista_de_tarefas.txt', 'w', encoding='utf-8') as arquivo_saida:
                arquivo_saida.write('\n'.join(['!' + tarefa for tarefa in lista_tarefas]))
            break
        
        else:
            lista_tarefas.append(usuario)

    except IndexError as error:
        print('nao ha o que ser refeito!')
