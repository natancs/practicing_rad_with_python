
from view.login_view import TelaLogin

# # Cria a janela de login
import customtkinter

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
app = TelaLogin(root)

# Inicia o loop da aplicação
root.mainloop()
