from tkinter import *
from ttkthemes import ThemedTk
import os

pastaAPP = os.path.dirname(__file__)

def formulario_cor(nome=None):
    exec(open(pastaAPP+"\\Formulario_cor.py").read(), {"nome": nome})

def formulario_grupo(nome=None):
    exec(open(pastaAPP+"\\Formulario_grupo.py").read(), {"nome": nome})


janela = ThemedTk(theme="breeze")
janela.title("Projeto python")
janela.geometry('1024x600')

#cria a barra de menu
barraMenu = Menu(janela)

#cria o menu e coloca na barra de menu
menu = Menu(barraMenu, tearoff=0)

#cria os itens do menu
menu.add_command(label="Cor", command=formulario_cor)
menu.add_command(label="Grupo", command=formulario_grupo)
menu.add_command(label="Sub-grupo", command=formulario_cor)

#definir o menu
barraMenu.add_cascade(label="Cadastros", menu=menu)

#colocar o mneu na janela
janela.config(menu=barraMenu)

janela.mainloop()
