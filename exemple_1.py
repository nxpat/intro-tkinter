#
# Crée une fenêtre simple avec un message et un bouton centrés
#
import tkinter as tk

window = tk.Tk()
window.title("Hello wold")  # titre de la fenêtre
window.geometry("300x300")  # dimensions de la fenêtre

hello = tk.Label(text="Hello world!")
hello.pack()  # label centré sur une ligne
button = tk.Button(text="Click me!")
button.pack()

tk.mainloop()