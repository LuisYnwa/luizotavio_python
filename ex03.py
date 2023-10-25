perguntinhas = [
    {
        'Pergunta': 'Quanto é 5 + 5?',
        'opcoes': ['1', '3', '10', '5'],
        'Resposta': (2),
    },
    {
        'Pergunta': 'Quem descobriu a América?',
        'opcoes': ['Chaves e Chapolin', 'Mohamed Salah', 'Cristóvão Colombo', 'Jacir'],
        'Resposta': (2),
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'opcoes': ['4', '5', '2', '1'],
        'Resposta': (1),
    },
]

contador_acertos = 0
for p in perguntinhas:
    print('Pergunta', p['Pergunta'])
    print()

    OPCOES = p['opcoes']
    for i, opcao in enumerate(OPCOES):
        print(f'{i})', opcao)

    qntd_opcoes = len(OPCOES)
    escolha_int = None
    acertou = False

    resposta = input('Digite o número da resposta ( ): ')
    if resposta.isdigit():
        escolha_int = int(resposta)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int <= qntd_opcoes:
            if escolha_int == p['Resposta']:
                acertou = True
                print('Você acertou!')
                contador_acertos += 1
            else:
                print('Você errou.')

print(f'Você acertou no total {contador_acertos} de {len(p)} perguntas !!')
