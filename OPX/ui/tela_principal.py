import tkinter as tk
from ui.novo_produto import novo_produto
from ui.gerar_programacao import gerar_programacao

def iniciar():

    janela = tk.Tk()
    janela.title("OPX")
    janela.geometry("500x500")

    rotulo = tk.Label(janela,
        text="Programação",
        font=("Arial", 12))

    rotulo.pack(pady=20)

    novoproduto = tk.Button(janela,
        text="Novo Produto",
        font=("Arial", 10, "bold"),
        width=15,
        command=lambda: novo_produto(janela))
    novoproduto.place(x=10, y=100)

    gerarprogramacao = tk.Button(janela,
        text="Gerar Programção",
        font=("Arial", 10, "bold"),
        width=15,
        command=lambda: gerar_programacao(janela))
    gerarprogramacao.place(x=10, y=140)
    



    janela.mainloop()