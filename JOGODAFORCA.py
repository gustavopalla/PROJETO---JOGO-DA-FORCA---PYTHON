import os
import time

palavras_secreta = ['futebol', 'python', 'codigo', 'java', 'debbugar']

while True:
    letras_acertadas = ''
    tentativas = 0

    print('Bem-vindo ao jogo da forca!')
    print('Você precisa escolher uma palavra secreta da lista e adivinhar qual é!')
    print('\n' * 3)
    time.sleep(2)
    os.system('cls')
    print('Carregando palavras secretas...')
    time.sleep(2)
    os.system('cls')
    time.sleep(2)

    print("Escolha uma palavra:")
    for i in range(len(palavras_secreta)):
        print(f"{i + 1}. Palavra {i + 1}")

    escolha = int(input("Digite o número da palavra que você deseja escolher: "))

    if 1 <= escolha <= len(palavras_secreta):
        palavra_secreta = palavras_secreta[escolha - 1]
    else:
        print("Escolha inválida, usando a primeira palavra!")
        palavra_secreta = palavras_secreta[0]

    print('O jogo começou!')
    time.sleep(1)

    while True:
        letra_digitada = input('Digite uma letra: ').lower()
        tentativas += 1

        if len(letra_digitada) > 1:
            print('Digite apenas uma letra!')
            continue

        if letra_digitada in palavra_secreta:
            if letra_digitada not in letras_acertadas:
                letras_acertadas += letra_digitada
            else:
                print('Você já digitou essa letra!')
        else:
            print('Letra errada! Tente novamente.')

        palavra_formada = ''

        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'

        print('Palavra formada:', palavra_formada)

        if palavra_formada == palavra_secreta:
            print('Você ganhou!')
            print('A palavra formada é:', palavra_formada)
            print('Seu número de tentativas foi:', tentativas)
            print('Limpando a tela para a próxima rodada...')
            time.sleep(3)
            os.system('cls')
            break

    jogar_novamente = input("Você quer jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        print("Obrigado por jogar!")
        break