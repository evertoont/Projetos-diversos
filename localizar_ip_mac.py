import tkinter as tk
from tkinter.messagebox import showinfo
from getmac import getmac
import socket


def ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    showinfo("Endereço IP", ip)


def mac():
    mac = getmac.get_mac_address()
    showinfo("Endereço MAC", mac)


def main():
    janela = tk.Tk()
    janela.config(bg="#000")
    janela.geometry('300x80')
    janela.title("Endereço IP e MAC")
    botao_ip = tk.Button(janela, width=23, text="Mostrar IP",
                         bg="#fff", fg="#000", font=("arial", 16, "bold"), command=ip)
    botao_ip.pack()
    botao_mac = tk.Button(janela, width=23, text="Mostrar MAC",
                          bg="#fff", fg="#000", font=("arial", 16, "bold"), command=mac)
    botao_mac.pack()

    janela.mainloop()


if __name__ == '__main__':
    main()
