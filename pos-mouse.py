import pyautogui
import tkinter as tk
from tkinter import StringVar

def atualizar_posicao():
    # Pega a posição atual do mouse
    x, y = pyautogui.position()
    texto.set(f"Posição do mouse:\nX = {x}, Y = {y}")
    # Atualiza a cada 100 ms
    root.after(100, atualizar_posicao)

# Cria a janela
root = tk.Tk()
root.title("Posição do Mouse")
root.geometry("200x100")
root.resizable(False, False)

# Variável de texto dinâmica
texto = StringVar()
label = tk.Label(root, textvariable=texto, font=("Arial", 12))
label.pack(expand=True)

# Inicia atualização
atualizar_posicao()

# Mostra a janela
root.mainloop()
