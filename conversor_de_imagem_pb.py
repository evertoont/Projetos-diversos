'''
- Necessário instalar a lib Pillow
- pip install Pillow

'''

from PIL import Image

def converter(caminho):

    try:
        with Image.open(caminho) as abrir_imagee:

            converter_pbb = abrir_imagee.convert('L')

            converter_pbb.show()

            print('Imagem convertida com sucesso!')
    except:
        print("Erro ao converter imagem, verifique o caminho indicado!")


print("""
======================================================
Digite abaixo o caminho de onde se encontra a imagem.

Exemplo: C:\\Users\\NOME_USUARIO\\imagens\\foto.png'
======================================================
""")


caminho_imagem = input("Digite o caminho da imagem: ").strip()

converter(caminho_imagem)