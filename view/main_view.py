import customtkinter as ctk
from tkinter import ttk
from CTkTable import *
from utils.check_status import check_status
from utils.save_data import save_data
from utils.calculate_average import calculate_average
from utils.loading_data import loading_data


class MainView:
    def __init__(self, win) -> None:
        win.title("Bem Vindo ao RAD")
        win.geometry("820x600+10+10")

        # componentes
        self.lblNome = ctk.CTkLabel(win, text="Nome do Aluno:")
        self.lblNota1 = ctk.CTkLabel(win, text="Nota 1:")
        self.lblNota2 = ctk.CTkLabel(win, text="Nota 2:")
        self.lblMedia = ctk.CTkLabel(win, text="Média:")
        self.txtNome = ctk.CTkEntry(win)
        self.txtNota1 = ctk.CTkEntry(win)
        self.txtNota2 = ctk.CTkEntry(win)
        self.btnCalcular = ctk.CTkButton(
            win, text="Calcular Média", command=self.fCalcularMedia)

        # ---- Componente TreeView ----
        self.dadosCulunas = ("Aluno", "Nota1", "Nota2", "Média", "Situação")
        self.treeMedias = CTkTable(
            master=win, column=5, corner_radius=3)
        self.treeMedias.delete_rows([0, 1])
        self.treeMedias.add_row(self.dadosCulunas)
        self.test = self.treeMedias.get_row(0)

        # self.verscrlbar = ttk.Scrollbar(win,
        #                                 orient="vertical",
        #                                 command=self.treeMedias.yview)
        # self.verscrlbar.pack(side='right', fill='x')

        # self.treeMedias.configure(yscrollcommand=self.verscrlbar.set)
        self.treeMedias.pack(expand=True, fill="both", padx=10, pady=10)

        # ------ Posicionando os componentes ------
        self.lblNome.place(x=100, y=50)
        self.txtNome.place(x=200, y=50)

        self.lblNota1.place(x=100, y=100)
        self.txtNota1.place(x=200, y=100)

        self.lblNota2.place(x=100, y=150)
        self.txtNota2.place(x=200, y=150)

        self.btnCalcular.place(x=100, y=200)

        self.treeMedias.place(x=100, y=300)
        # self.verscrlbar.place(x=805, y=300, height=225)

        self.id = 0
        self.iid = 0

        self.carregarDadosIniciais()

    def carregarDadosIniciais(self):
        loading_data(self)

    def fSalvarDados(self):
        save_data(self)

    def fCalcularMedia(self):
        calculate_average(self)


# self.treeMedias.heading("Aluno", text="Aluno")
        # self.treeMedias.heading("Nota1", text="Nota 1")
        # self.treeMedias.heading("Nota2", text="Nota 2")
        # self.treeMedias.heading("Média", text="Média")
        # self.treeMedias.heading("Situação", text="Situação")
# self.treeMedias.column("Aluno", minwidth=0, width=100)
        # self.treeMedias.column("Nota1", minwidth=0, width=100)
        # self.treeMedias.column("Nota2", minwidth=0, width=100)
        # self.treeMedias.column("Média", minwidth=0, width=100)
        # self.treeMedias.column("Situação", minwidth=0, width=100)
