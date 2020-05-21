import tkinter
from time import strftime


# Criando janela do relógio e sua configurações

janela = tkinter.Tk()
janela.title('Relógio Digital')
janela.geometry('350x100+500+300')

relogio = tkinter.Label(width=20, height=20)
relogio.place(x=150, y=150)
relogio['font'] = 'Arial 55 bold'
relogio['background'] = 'black'
relogio['foreground'] = 'white'
relogio.pack(anchor = 'center')


# Função responsável por atualizar as horas

def atualiza_horas():
    hora_atual = strftime('%H:%M:%S')
    relogio.config( text = hora_atual)
    relogio.after(1000, atualiza_horas)


# Executando relógio
atualiza_horas()

janela.mainloop()