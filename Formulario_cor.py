from random import randint
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from ttkthemes import ThemedTk
import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cor(
    
        id INT PRIMARY KEY,
        nome TEXT NOT NULL   
    )
""")
conn.commit()



def salvarCor():
   if txtNome.get() == "":
       showerror("Erro!!", "Preecha os campos")
   else:
       id = randint(1, 99999)
       nome = txtNome.get()
       showinfo("Sucesso!!", f"Nome da cor : {nome}\n"
                             f"Id da cor : {id}")

       cursor.execute("""
        INSERT INTO cor(id, nome)VALUES(?,?)
       """, (id, nome))
       conn.commit()
       showinfo("Sucesso!!", "Dados salvos com sucesso!!")



janela = ThemedTk(theme="breeze")
janela.title("Cadastro de cores")
janela.geometry('300x100')
janela.resizable(False, False)

#inicio do frame
frame = ttk.Frame(janela, borderwidth=1, width=100, height=50)

#label
label = ttk.Label(frame, text="Nome da cor : ")
label.place(x=3, y=15)

#campo nome
txtNome = ttk.Entry(janela, font=16)
txtNome.place(x=100, y=10)

#botao
btnSlavar = ttk.Button(janela, text="Salvar cor", command=salvarCor)
btnSlavar.place(x=5, y=60)

frame.grid(row=0, column=0)



janela.mainloop()
