# Crée une fenêtre simple avec un message et un bouton centrés
#
import tkinter as tk

mon_app = tk.Tk()

texte = tk.Label(mon_app, text='Bonjour tout le monde !', fg='red')
texte.grid(row=0, column=0)

texte = tk.Label(mon_app, text='Hello!', fg='blue')
texte.grid(row=0, column=1)

# Bouton avec une fonction de rappel
bouton = tk.Button(mon_app, text='Quitter', command = mon_app.destroy)
bouton.grid(row=1, column=0)

mon_app.mainloop()