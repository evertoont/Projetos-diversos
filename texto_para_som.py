'''
- Necessário instalar as libs Pygame e gTTS

- pip install pygame
- pip install gTTS

'''

import io
import os
import pygame
from gtts import gTTS


def falar_texto(texto, opcao):

    if opcao == 1:
        with open('audio.mp3', 'wb') as arquivo:
            gTTS(text=texto, lang="pt-br").write_to_fp(arquivo)
    else:
        with io.BytesIO() as arquivo:
            gTTS(text=texto, lang="pt-br").write_to_fp(arquivo)
            arquivo.seek(0)
            pygame.mixer.init()
            pygame.mixer.music.load(arquivo)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue


def main():

    while True:
        os.system("cls || clear")

        opcao = int(input('''
        [1] Salvar arquivo de audio
        [2] Apenas ouvir o audio 
        
        Escolha sua opção: '''))

        if opcao == 1 or opcao == 2:
            texto = input("\nDigite o que você deseja ouvir/salvar em audio: ")
            break
        else:
            continue

    falar_texto(texto, opcao)


if __name__ == '__main__':
    main()
