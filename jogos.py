import forca
import main


def escolher_jogo():
    print('*******************************')
    print('******Escolha o seu jogo*******')
    print('*******************************')

    print('(1) Forca (2) Adivinhação!!!')
    jogo = int(input('Informe o jogo: '))

    if jogo == 1:
        print('Jogando forca')
        forca.jogar()
    elif jogo == 2:
        print('Jogando Adivinhação')
        main.jogar()


if __name__ == '__main__':
    escolher_jogo()

