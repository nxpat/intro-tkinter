# Introduction à Tkinter : exercice

Réaliser une application d'apparence semblable à l'image `exercice.png`.

![Programmation événementielle](https://raw.githubusercontent.com/nxpat/intro-tkinter/refs/heads/main/exercice.png)

# Introduction à Tkinter : éléments de cours

Nous allons créer une fenêtre très simple, et y ajouter deux composants graphiques (widgets) typiques : un texte (ou label) et un bouton (ou button).

## Un permier exemple simple

```python
import tkinter as tk  # Importation de la bibliothèque Tkinter pour créer des interfaces graphiques

# Création de la fenêtre principale
window = tk.Tk()  
window.title("Hello world")  # Définition du titre de la fenêtre
window.geometry("300x300")  # Définition de la taille de la fenêtre (300 pixels de large et 300 pixels de haut)

# Création d'un label avec le texte "Hello world!"
hello = tk.Label(text="Hello world!")  
hello.pack()  # Ajout du label à la fenêtre avec un espacement automatique

# Création d'un bouton avec le texte "Click me!"
button = tk.Button(text="Click me!")  
button.pack()  # Ajout du bouton à la fenêtre avec un espacement automatique

# Lancement de la boucle principale, qui écoute les événements (clics, entrées, etc.)
tk.mainloop()

```

## Un exemple avec plus d'interaction

```python
import tkinter as tk

# Création de la fenêtre principale de l'application
mon_app = tk.Tk()  

# Création d'un label avec le texte 'Bonjour tout le monde !' et couleur rouge
texte = tk.Label(mon_app, text='Bonjour tout le monde !', fg='red')  
# Placement du label dans la grille à la position (0, 0) (ligne 0, colonne 0)
texte.grid(row=0, column=0)  

# Création d'un bouton avec le texte 'Quitter' qui ferme l'application
# La fonction command appelle mon_app.destroy pour fermer la fenêtre
bouton = tk.Button(mon_app, text='Quitter', command=mon_app.destroy)  
# Placement du bouton dans la grille à la position (1, 0) (ligne 1, colonne 0)
bouton.grid(row=1, column=0)  

# Lancement de la boucle principale qui écoute les événements (clics, mouvements, etc.)
mon_app.mainloop()  
```

### Explications du code

### Ligne 1
```python
import tkinter as tk
``` 
Importe le module `tkinter`. Pour accéder aux fonctionnalités de ce module (propriétés et méthodes) il faudra faire précéder le nom de la commande du préfixe `tk`.

### Ligne 2
```python
mon_app = tk.Tk()
``` 
Crée un objet `mon_app` qui prend la forme d'une fenêtre graphique `Tkinter`.

### Ligne 3
```python
texte = tk.Label(mon_app, text='Bonjour tout le monde !', fg='red')
``` 
créé un objet (un widget) `texte`, à partir de la classe `Label()`. Cette classe permet d'afficher des messages à l'intérieur d'une fenêtre. Nous fournissons trois arguments ici :

- `mon_app` : indique que le nouveau widget que nous sommes en train de créer sera contenu dans un autre widget préexistant, que nous désignons comme le parent (on peut dire aussi que l'objet texte est un enfant de l'objet `mon_app`). Dans cet exemple, le widget `texte` est un enfant de notre fenêtre d'application `mon_app`.
- les deux arguments suivants précisent le texte de l'étiquette `text` et sa couleur d'avant-plan (ou _foreground_, en abrégé `fg`). Nous pourrions préciser d'autres caractéristiques : la police à utiliser, ou la couleur d'arrière-plan, par exemple.

### Ligne 4
```python
texte.grid(row=0, column=0)
``` 
active la méthode du gestionnaire de positionnement `grid()`. Celle-ci permet de positionner les widgets dans la fenêtre parent. Il ne faut pas oublier d'invoquer cette méthode sinon le widget n'apparaîtra pas sur notre fenêtre application puisque `TKinter` ne saura pas comment positionner notre `texte` dans la fenêtre.

### Ligne 5
```python
bouton = tk.Button(mon_app text='Quitter', command = mon_app.destroy)
``` 
Crée un second widget enfant (un bouton) avec la commande TKinter `tk.Button()`. Comme il s'agit cette fois d'un objet interactif, nous devons préciser avec l'option `command` l'action à exécuter lorsque l'utilisateur effectue un clic sur le bouton. Ici, nous appellons `mon_app.destroy()`, qui ferme la fenêtre parent. `mon_app.destroy()` est appelée une **fonction de rappel**. Remarquer l'abscence de parenthèses.

### Ligne 6
```python
bouton.grid(row=1, column=0)
```
place le bouton dans la fenêtre d'application : dans la même colonne (`column=0`) que le widget `texte` , mais à la ligne n°1 (`row=1`), c'est-à-dire en dessous.

### Ligne 7
```python
mon_app.mainloop()
```
lance l'application. C'est cette commande qui démarre gestionnaire d'événements associé à la fenêtre `mon_app`. 

`mainloop` est une boucle infinie qui attend en permanence en tâche de fond un événement, émis par l'utilisateur ou le système d'exploitation de l'ordinateur. Le système interroge sans cesse son environnement, notamment au niveau des périphériques d'entrée (souris, clavier, etc.). Lorsqu'un événement est détecté, une action est exécutée.

Essayer de relancer le programme précédent en retirant la dernière ligne. Que se passe t-il ?

# Programmes pilotés par événements 

Dans les programmes Python réalisés jusqu'à présent, l'éxécution se déroulait de manièrre linéaire du début à la fin. Souvent, on commence par initialiser des variables, puis on exécute une ou plusieurs actions dans un ordre bien défini et enfin, on affiche le résultat dans la console.

Dans le cas d’un programme qui utilise une interface utilisateur (souvent graphique), par contre, tout est différent. Le programme est piloté par les événements. Après la phase d’initialisation, un programme avec une interface utilisateur se met en « en attente », et passe la main à un autre logiciel, intégré au système d’exploitation de la machine et « tourne » en permanence.

On parle de **programmation événementielle**.

![Programmation événementielle](https://profjahier.github.io/html/NSI/tkinter/tkinter_Lecluse/helloworld/prog_evt.png)

Le gestionnaire d’événements scrute sans cesse tous les périphériques (clavier, souris, etc.) et réagit immédiatement lorsqu’un événement y est détecté. Un tel événement peut être une action quelconque de l’utilisateur : déplacement de la souris, appui sur une touche, etc., mais aussi un événement externe ou un automatisme (top d’horloge, par ex.) Lorsqu’il détecte un événement, le gestionnaire envoie un message au programme, lequel doit être conçu pour réagir en conséquence. Dans le cas d’un programme avec une interface graphique, l’ordre dans lequel les fonctions sont appelées n’est plus défini par le programme, mais par des événements externes !

# Interaction graphique
Voici des exemples pour créer différentes fonctionnalités : affichage de texte, zone d'entrée de texte, curseur, menu déroulant, et affichage de points, lignes ou rectangles.

## Exemple 1: Affichage de texte

Cet exemple crée une fenêtre avec un texte affiché.

```python
import tkinter as tk

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Affichage de texte")

# Affichage du texte dans un label
label = tk.Label(fenetre, text="Bienvenue dans Tkinter!", font=("Arial", 16))
label.pack(pady=20)

# Lancement de la boucle principale
fenetre.mainloop()
```

---

## Exemple 2: Zone d'entrée de texte

Voici un exemple avec une zone d'entrée de texte où l'utilisateur peut saisir du texte.

```python
import tkinter as tk

def afficher_texte():
    texte = zone_texte.get("1.0", tk.END)
    print("Texte entré :", texte)

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Zone d'entrée de texte")

# Création d'une zone d'entrée de texte
zone_texte = tk.Text(fenetre, height=10, width=40)
zone_texte.pack(pady=10)

# Bouton pour afficher le texte
bouton = tk.Button(fenetre, text="Afficher le texte", command=afficher_texte)
bouton.pack(pady=5)

# Lancement de la boucle principale
fenetre.mainloop()
```

---

## Exemple 3: Curseur

Cet exemple crée une fenêtre avec un curseur simple pour ajuster une valeur.

```python
import tkinter as tk

def afficher_valeur(val):
    label.config(text=f"Valeur : {val}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Curseur")

# Création d'un label pour afficher la valeur
label = tk.Label(fenetre, text="Valeur : 0", font=("Arial", 14))
label.pack(pady=20)

# Création d'un curseur
curseur = tk.Scale(fenetre, from_=0, to=100, orient=tk.HORIZONTAL, command=afficher_valeur)
curseur.pack(pady=10)

# Lancement de la boucle principale
fenetre.mainloop()
```

---

## Exemple 4: Menu déroulant

Dans cet exemple, un menu déroulant permet de sélectionner une option.

```python
import tkinter as tk

def afficher_selection(val):
    print("Sélection : ", val)

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Menu déroulant")

# Liste des options
options = ["Option 1", "Option 2", "Option 3"]

# Variable pour stocker la sélection
selection = tk.StringVar(fenetre)
selection.set(options[0])  # Valeur par défaut

# Création d'un menu déroulant
menu_deroulant = tk.OptionMenu(fenetre, selection, *options, command=afficher_selection)
menu_deroulant.pack(pady=20)

# Lancement de la boucle principale
fenetre.mainloop()
```

---

## Exemple 5: Affichage de points et lignes ou rectangles

Cet exemple montre comment afficher un cercle et un rectangle sur un canevas.

```python
import tkinter as tk

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Affichage de formes")

# Création d'un canevas
canevas = tk.Canvas(fenetre, width=400, height=400, bg="white")
canevas.pack()

# Dessin d'une ligne
canevas.create_line(50, 50, 350, 50, fill="blue", width=2)

# Dessin d'un rectangle
canevas.create_rectangle(100, 100, 300, 300, outline="red", fill="lightblue")

# Dessin d'un cercle
canevas.create_oval(150, 150, 250, 250, outline="green", fill="yellow")

# Lancement de la boucle principale
fenetre.mainloop()
```

---

# Écouteurs d'événement

Voici quelques exemples d'écouteurs d'événements pour la souris et le clavier.

Ces exemples montrent comment interagir avec les événements de la souris et du clavier dans une application Tkinter. Vous pouvez développer ces concepts pour créer des interfaces utilisateur plus complexes et réactives !

## Écouteurs d'événements de la souris

### Exemple 1: Cliquer sur un bouton

Cet exemple montre comment réagir à un clic de souris sur un bouton.

```python
import tkinter as tk

def on_click(event):
    print(f"Clic détecté à la position ({event.x}, {event.y})")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Écouteur de clic de souris")

# Création d'un bouton
bouton = tk.Button(fenetre, text="Cliquez ici")
bouton.pack(pady=20)

# Lier l'événement de clic de souris à la fonction on_click
bouton.bind("<Button-1>", on_click)

# Lancement de la boucle principale
fenetre.mainloop()
```

---

### Exemple 2: Déplacement de la souris

Cet exemple détecte le mouvement de la souris sur l'application.

```python
import tkinter as tk

def on_move(event):
    print(f"Souris déplacée à la position ({event.x}, {event.y})")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Écouteur de mouvement de souris")

# Lier l'événement de mouvement de souris à la fonction on_move
fenetre.bind("<Motion>", on_move)

# Lancement de la boucle principale
fenetre.mainloop()
```

---

## Écouteurs d'événements du clavier

### Exemple 3: Touche pressée

Cet exemple montre comment réagir à une touche pressée sur le clavier.

```python
import tkinter as tk

def on_key_press(event):
    print(f"Touche pressée : {event.char}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Écouteur de pression de touche")

# Lier l'événement de pression de touche à la fonction on_key_press
fenetre.bind("<KeyPress>", on_key_press)

# Lancement de la boucle principale
fenetre.mainloop()
```

---

### Exemple 4: Touche relâchée

Cet exemple détecte lorsque des touches sont relâchées.

```python
import tkinter as tk

def on_key_release(event):
    print(f"Touche relâchée : {event.char}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Écouteur de relâchement de touche")

# Lier l'événement de relâchement de touche à la fonction on_key_release
fenetre.bind("<KeyRelease>", on_key_release)

# Lancement de la boucle principale
fenetre.mainloop()
```

---

Voici une liste des écouteurs d'événements communs dans Tkinter pour interagir avec les événements de la souris et du clavier :

## Écouteurs d'événements pour la souris

- **`<Button-1>`** : Clic gauche de la souris.
- **`<Button-2>`** : Clic du bouton central (roue de la souris).
- **`<Button-3>`** : Clic droit de la souris.
- **`<Double-Button-1>`** : Double-clic gauche de la souris.
- **`<Triple-Button-1>`** : Triple-clic gauche de la souris.
- **`<Motion>`** : Mouvement de la souris.
- **`<Enter>`** : La souris entre dans un widget.
- **`<Leave>`** : La souris quitte un widget.
- **`<MouseWheel>`** : Défilement de la roulette de la souris.

## Écouteurs d'événements pour le clavier

- **`<KeyPress>`** : Touche pressée (toutes les touches).
- **`<KeyRelease>`** : Touche relâchée (toutes les touches).
- **`<Return>`** : Touche Entrée.
- **`<BackSpace>`** : Touche Retour arrière.
- **`<Tab>`** : Touche Tabulation.
- **`<Escape>`** : Touche Échap.
- **`<Delete>`** : Touche Supprimer.
- **`<Home>`** : Touche Début.
- **`<End>`** : Touche Fin.
- **`<Left>`** : Touche Flèche gauche.
- **`<Right>`** : Touche Flèche droite.
- **`<Up>`** : Touche Flèche haut.
- **`<Down>`** : Touche Flèche bas.

## Écouteurs d'événements de fenêtre

- **`<Configure>`** : Changement de la taille ou de la position de la fenêtre.
- **`<Visibility>`** : Changements de visibilité de la fenêtre (apparaît ou disparaît).
- **`<FocusIn>`** : L'entrée obtient le focus.
- **`<FocusOut>`** : L'entrée perd le focus.

## Écouteurs d'événements divers

- **`<Expose>`** : La zone est redessinée.
- **`<Motion>`** : Mouvement de la souris.
- **`<Scrollbar>`** : Utilisation du défilement.

---

# Documentation sur Tkinter
[(FR) Documention de Jahier](https://profjahier.github.io/html/NSI/tkinter/index.html)

[(EN) Tutoriel officiel tkdocs](https://tkdocs.com/tutorial/index.html)

[(EN) Tutoriel de PythonTutorial.net](https://www.pythontutorial.net/tkinter/tkinter-window/)

[(EN) Tutoriel de New Mexico Tech](https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html)

  
