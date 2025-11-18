import tkinter as tk
import json
import os

def gerar_programacao(janela):
    janelaprogramacao = tk.Frame(janela,
                         bg="blue",
                         width=600,
                         height=600)
    janelaprogramacao.place(x=150, y=100)

    titulo_nome = tk.Label(janelaprogramacao,
                    text="Produto",
                    font=("Arial", 11))
    titulo_nome.place(x=20, y=20)

    produto = tk.Entry(janelaprogramacao,
                    width=30,
                    font=("Arial", 11))
    produto.place(x=100, y=20)

    quantidade_nome = tk.Label(janelaprogramacao,
                    text="Quantidade",
                    font=("Arial", 11))
    quantidade_nome.place(x=20, y=60)

    quantidade = tk.Entry(janelaprogramacao,
                    width=30,
                    font=("Arial", 11))
    quantidade.place(x=110, y=60)


    gerar = tk.Button(janelaprogramacao,
                    text = "Gerar",
                    command = lambda: print("Gerando..."))
    gerar.place(x=100, y=200)



    def salvar_programacao(produto_entry, quantidade_entry):
        nome = produto_entry.get()
        qtd = quantidade_entry.get()
        
        if not os.path.exists("data"):
            os.makedirs("data")
        
        arquivo = "data/programacao.json"
        
        if os.path.exists(arquivo):
            with open(arquivo, "r") as f:
                dados = json.load(f)
        else:
            dados = []
        
        # Adiciona novo item com produto E quantidade
        dados.append({"produto": nome, "quantidade": qtd})
        
        with open(arquivo, "w") as f:
            json.dump(dados, f, indent=4)
        
        print("Programação salva!")

    # No botão Gerar:
    gerar = tk.Button(janelaprogramacao,
                    text="Gerar",
                    command=lambda: salvar_programacao(produto, quantidade))