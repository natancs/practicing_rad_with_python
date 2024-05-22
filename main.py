import os
import customtkinter
from view.login_view import TelaLogin
from dotenv import load_dotenv

load_dotenv()
# # Cria a janela de login

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
app = TelaLogin(root)

# Inicia o loop da aplicação
root.mainloop()
