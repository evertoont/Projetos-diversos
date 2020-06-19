import tkinter as tk
from PIL import Image, ImageTk


def carregarImagem(diretorio):
    with Image.open(diretorio) as Imagem:
        renderizar = ImageTk.PhotoImage(Imagem)
        img = tk.Label(image=renderizar)
        img.image = renderizar
        img.place(x=0, y=0)
        return Imagem.size


def main():
    print('\nDigite o diretório da imagem abaixo (Siga o exemplo)')
    print("Exemplo -> C:\\Users\\YourName\\Pictures\\avatar.png: ")

    diretorio = input("URL: ")
    root = tk.Tk()
    altura, largura = carregarImagem(diretorio)
    root.wm_title('Visualizador de imagem')
    root.geometry(f"{altura}x{largura}")
    root.mainloop()


if __name__ == '__main__':
    main()
