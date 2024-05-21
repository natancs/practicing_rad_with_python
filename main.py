import tkinter as tk
from main_view import MainView

windows = tk.Tk()
windows.title("Bem Vindo ao RAD")
windows.geometry("820x600+10+10")
MainView(windows)

windows.mainloop()
