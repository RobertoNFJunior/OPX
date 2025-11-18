import tkinter as tk   
import json
import os

def salvar_produto(produto_entry):
    nome = produto_entry.get()

    if not os.path.exists("data"):
        os.makedirs("data")

    dados = {"produto": nome}

    with open("data/produto.json", "a") as save:
        json.dump(dados, save, indent=4)

    print("Salvo!!!")

def novo_produto(janela):
    container = tk.Frame(janela,
                         bg="black",
                         width=600,
                         height=600)
    container.place(x=150, y=100)

    nome_produto = tk.Label(container,
                    text="Produto",
                    font=("Arial", 12))
    nome_produto.place(x=20, y=20)

    produto = tk.Entry(container,
                    width=30,
                    font=("Arial", 12))
    produto.place(x=100, y=20)

    salvar = tk.Button(container,
                    text = "Salvar",
                    command = lambda: salvar_produto(produto))
    salvar.place(x=100, y=60)
