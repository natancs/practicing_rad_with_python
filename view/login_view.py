import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from view.main_view import MainView


class TelaLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x250")

        self.text = ctk.CTkLabel(root, text="Fazer Login")
        self.text.pack_configure(padx=10, pady=10)
        self.entry_username = ctk.CTkEntry(root, placeholder_text="E-mail")
        self.entry_username.pack(padx=10, pady=10)

        self.entry_password = ctk.CTkEntry(
            root, placeholder_text="Senha", show="*")
        self.entry_password.pack(padx=10, pady=10)

        self.button_login = ctk.CTkButton(
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
            nova_janela = ctk.CTkToplevel()
            app = MainView(nova_janela)

        else:
            CTkMessagebox(
                title="Erro", message="Credenciais incorretas", icon="cancel")
