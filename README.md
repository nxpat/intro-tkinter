# intro-tkinter
Introduction à Tkinter

# Exercice

Réaliser une application d'apparence semblable à l'image `exercice.png`.

# Introduction à Tkinter 

Nous allons créer une fenêtre très simple, et y ajouter deux composants graphiques (widgets) typiques : un bout de texte (ou label) et un bouton (ou button).

## Un permier exemple simple

```python
import tkinter as tk

window = tk.Tk()
window.title("Hello wold")
window.geometry("300x300")

hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()

tk.mainloop()
```

## Un exemple avec plus d'interaction

```python
import tkinter as tk

mon_app = tk.Tk()

texte = tk.Label(mon_app, text='Bonjour tout le monde !', fg='red')
texte.grid(row=0, column=0)

# Bouton avec une fonction de rappel
bouton = tk.Button(mon_app, text='Quitter', command = mon_app.destroy)
bouton.grid(row=1, column=0)

mon_app.mainloop()
```

### Explications

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
  

## Documentation sur Tkinter
[(FR) Documention de Jahier](https://profjahier.github.io/html/NSI/tkinter/index.html).

[(EN) Tutoriel officiel tkdocs](https://tkdocs.com/tutorial/index.html).

[(EN) Tutoriel de PythonTutorial.net](https://www.pythontutorial.net/tkinter/tkinter-window/).

[(EN) Tutoriel de New Mexico Tech](https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html)

  
