import tkinter as tk
from tkinter import ttk
from utils.index import *


class MainView:
    def __init__(self, win) -> None:
        # componentes
        self.lblNome = tk.Label(win, text="Nome do Aluno:")
        self.lblNota1 = tk.Label(win, text="Nota 1:")
        self.lblNota2 = tk.Label(win, text="Nota 2:")
        self.lblMedia = tk.Label(win, text="Média:")
        self.txtNome = tk.Entry(bd=3)
        self.txtNota1 = tk.Entry()
        self.txtNota2 = tk.Entry()
        self.btnCalcular = tk.Button(
            win, text="Calcular Média", command=self.fCalcularMedia)

        # ---- Componente TreeView ----
        self.dadosCulunas = ("Aluno", "Nota1", "Nota2", "Média", "Situação")
        self.treeMedias = ttk.Treeview(win,
                                       columns=self.dadosCulunas,
                                       selectmode="browse")

        self.verscrlbar = ttk.Scrollbar(win,
                                        orient="vertical",
                                        command=self.treeMedias.yview)
        self.verscrlbar.pack(side='right', fill='x')

        self.treeMedias.configure(yscrollcommand=self.verscrlbar.set)
        self.treeMedias.heading("Aluno", text="Aluno")
        self.treeMedias.heading("Nota1", text="Nota 1")
        self.treeMedias.heading("Nota2", text="Nota 2")
        self.treeMedias.heading("Média", text="Média")
        self.treeMedias.heading("Situação", text="Situação")

        self.treeMedias.column("Aluno", minwidth=0, width=100)
        self.treeMedias.column("Nota1", minwidth=0, width=100)
        self.treeMedias.column("Nota2", minwidth=0, width=100)
        self.treeMedias.column("Média", minwidth=0, width=100)
        self.treeMedias.column("Situação", minwidth=0, width=100)
        self.treeMedias.pack(padx=10, pady=10)

        # ------ Posicionando os componentes ------
        self.lblNome.place(x=100, y=50)
        self.txtNome.place(x=200, y=50)

        self.lblNota1.place(x=100, y=100)
        self.txtNota1.place(x=200, y=100)

        self.lblNota2.place(x=100, y=150)
        self.txtNota2.place(x=200, y=150)

        self.btnCalcular.place(x=100, y=200)

        self.treeMedias.place(x=100, y=300)
        self.verscrlbar.place(x=805, y=300, height=225)

        self.id = 0
        self.iid = 0

        self.carregarDadosIniciais()

    def carregarDadosIniciais(self):
        loading_data(self)

    def fSalvarDados(self):
        save_data(self)

    def fVerificarSituacao(self, nota1, nota2):
        return check_status(nota1, nota2)

    def fCalcularMedia(self):
        calculate_avarege(self)
