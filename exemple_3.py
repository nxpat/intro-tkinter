#
# Crée une fenêtre simple avec des sliders
#
import tkinter as tk

app = tk.Tk()

w = tk.Scale(app, from_=0, to=42)
w.pack()
w = tk.Scale(app, from_=0, to=200, orient=tk.HORIZONTAL)
w.pack()

#app.mainloop()

#
# Crée une fenêtre simple avec des sliders
# et un bouton pour récupérer leurs valeurs
#

# affiche la valeur des sliders dans la console
def show_values():
    print (w1.get(), w2.get())

app2 = tk.Tk()
app2.geometry("+100+50")  # dimensions de la fenêtre

w1 = tk.Scale(app2, from_=0, to=42)
w1.pack()
w2 = tk.Scale(app2, from_=0, to=200, orient=tk.HORIZONTAL)
w2.pack()
tk.Button(app2, text='Show', command=show_values).pack()

app2.mainloop()