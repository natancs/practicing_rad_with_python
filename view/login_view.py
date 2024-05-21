import tkinter as tk
from view.main_view import MainView
from tkinter import messagebox


class TelaLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x150")

        self.label_username = tk.Label(root, text="Usuário:")
        self.label_username.pack()
        self.entry_username = tk.Entry(root)
        self.entry_username.pack()

        self.label_password = tk.Label(root, text="Senha:")
        self.label_password.pack()
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack()

        self.button_login = tk.Button(
            root, text="Login", command=self.validar_login)
        self.button_login.pack(pady=10)

    def validar_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Verifica se as credenciais estão corretas
        if username == "admin" and password == "admin":
            # Fecha a tela de login
            self.root.withdraw()

            # Cria uma nova janela
            nova_janela = tk.Toplevel()
            app = MainView(nova_janela)

        else:
            messagebox.showerror("Erro", "Credenciais incorretas")
