import random

def jogar():

    print('*******************************')
    print('Bem vindo ao jogo de Advinhação')
    print('*******************************')

    # numero_secreto = round(random.random() * 100)
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000
    # rodada = 1

    print('Qual nivel de dificuldade? ')
    print('(1) Fácil \n(2) Médio \n(3) Dificil')

    nivel = int(input('Defina o nivel: '))
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5

    # while (rodada <= 3):
    for rodada in range(1, total_de_tentativas + 1):
        # print('tentati va ', rodada, 'de', total_de_tentativas)
        print('tentativa {0} de {1}'.format(rodada, total_de_tentativas))

        chute_str = input('Digite um número entre 1 e 100: ')
        chute_int = int(chute_str)

        if chute_int < 1 or chute_int > 100:
            print('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = numero_secreto == chute_int
        maior = chute_int > numero_secreto
        menor = chute_int < numero_secreto

        print('Você digitou ', chute_int)

        if acertou:
            print('Você acertou e fez {} pontos'.format(pontos))
            break
        else:
            if maior:
                print('Você errou! O seu chute foi maior')
            elif menor:
                print('Você errou! O seu chute foi menor')
            pontos_perdidos = abs(numero_secreto - chute_int)
            pontos = pontos - pontos_perdidos

    # rodada = rodada + 1

    print('Fim de Jogo!!!')

if __name__ == '__main__':
    jogar()
