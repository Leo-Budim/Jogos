import random

def imprime_mensagem_abertura():
    print('*******************************')
    print('  Bem vindo ao jogo de Forca')
    print('*******************************')

def carrega_palavra_secreta():
    palavras = []
    arquivo = open('palavras.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    letras_acertadas = ['_' for letra in palavra_secreta]
    return letras_acertadas

def pede_chute():
    chute = input('Informe a letra: ')
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(palavra_secreta, letras_acertadas, chute):
    index = 0
    for letra in palavra_secreta:
         if chute == letra:
             letras_acertadas[index] = letra
         index += 1
    print(letras_acertadas)

def marca_chute_errado(erros_cometidos, erros_permitidos):
    erros_cometidos += 1
    print('Você Errou! Faltam {} tentativas'.format(erros_permitidos - erros_cometidos))
    return erros_cometidos


def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros_permitidos = 6
    erros_cometidos = 0

    print(letras_acertadas)
    while (not enforcou and not acertou):

        chute = pede_chute()
        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, letras_acertadas, chute)
        else:
           erros_cometidos = marca_chute_errado(erros_cometidos, erros_permitidos)

        enforcou = erros_cometidos == erros_permitidos
        acertou = '_' not in letras_acertadas

    print(letras_acertadas)

    if acertou:
        print('Você ganhou!!!')
    elif enforcou:
        print("Você perdeu!!!")

    print('Fim de Jogo!!!')

if __name__ == '__main__':
    jogar()